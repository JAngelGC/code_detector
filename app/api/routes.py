from flask import Blueprint, jsonify, request, abort
from google.cloud.firestore_v1.base_query import FieldFilter
from typing import List, Dict
from app.utils.matcher import match_fingerprints, get_fingerprint, match_files
from app.files.files import get_absolute_file_path
from flask_cors import CORS
from app.api.firestore import db
from app.api.misc import jsonify_fingerprint, read_python_file
from app.api.interfaces import (Submission, KGramPosition, KGramHashMatch,
                                SubmissionSimilarity, SubmissionTable)

# Store all test files
file_paths: List[str] = get_absolute_file_path()
file_paths.sort()

tasks = Blueprint('tasks', __name__)
CORS(tasks)

# Get homework similarity
@tasks.route('/submission/<string:submission_id>/<string:homework_id>', methods=['GET'])
def get_submission_similarity(submission_id, homework_id):
    """
    """
    submissions_max_sim_ref = db.collection("submssion_max_similarity")
    query_ref = submissions_max_sim_ref.where(filter=FieldFilter("id", "==", submission_id))

    query_ref = query_ref.get()
    sub_simi_dict = query_ref[0].to_dict()
    
    return jsonify({
        "message": "Submission similarity retrieved successfully",
        "submission_similarity": sub_simi_dict
    }), 201


# Post a subbmission
@tasks.route('/submission', methods=['POST'])
def post_submission():
    try:
        if not request.json:
            abort(400)
        
        file_content: str = read_python_file(request.json["file_url"])


        fingerprint = get_fingerprint(file_content)
        homework_id: str = request.json["homework_id"]

        homework_sub = {
            "author": request.json["author"],
            "homework_id": homework_id,
            "file_name": request.json["file_name"],
            "file_url": request.json["file_url"],
            "content": file_content,
            "fingerprint": jsonify_fingerprint(fingerprint)
        }

        print("siuuuuuuuuuuuuuuu")
        update_time, submission_ref = db.collection("homework_submission").add(homework_sub)
        # Delete all documents in collection and make a new entry for each homework
        submissions_sim_ref = db.collection("submssion_max_similarity")
        query  = submissions_sim_ref.where(filter=FieldFilter("homeworkId", "==", homework_id))

        docs = query.get()

        for doc in docs:
            doc.reference.delete()


        # Fill homework_submission collection with new entries
        submissions_ref = db.collection("homework_submission")
        query_ref = submissions_ref.where(filter=FieldFilter("homework_id", "==", homework_id))
        query_ref = query_ref.get()
        for doc in query_ref:
            post_max_similarity(doc.id, homework_id)

        return jsonify({
            "message": "Homework submission saved successfully",
            "submission_id": submission_ref.id
        }), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Create a homework
@tasks.route('/homework', methods=['POST'])
def post_homework():

    try:
        if not request.json:
            abort(400)

        homework = {
            "name": request.json["name"]
        }

        update_time, hw_ref = db.collection("homework").add(homework)

        return jsonify({
            "message": "Homework created successfully",
            "homework_id": hw_ref.id
        }), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Get all homeworks
@tasks.route('/homework', methods=['GET'])
def get_homeworks():
    """
    """
    try:
        homeworks_ref = db.collection("homework").get()

        homeworks = []

        for hw in homeworks_ref:
            hw_dict: Dict = hw.to_dict()

            submissions_ref = db.collection("homework_submission")
            query_ref = submissions_ref.where(filter=FieldFilter("homework_id", "==", hw.id))
            query_ref = query_ref.get()

            hw_dict["submissions"] = len(query_ref)

            hw_dict["highSimilarity"] = 0
            hw_dict["mediumSimilarity"] = 0
            hw_dict["lowSimilarity"] = 0
            hw_dict["notSimilarity"] = 0

            for submission in query_ref:

                simmilarity_ref = db.collection("submssion_max_similarity")
                query_ref = simmilarity_ref.where(filter=FieldFilter("id", "==", submission.id))
                query_ref = query_ref.get()

                if(len(query_ref) != 1):
                    continue

                simmilarity_dict: Dict = query_ref[0].to_dict()

                if simmilarity_dict["similarity"] > 75:
                    hw_dict["highSimilarity"] += 1
                elif simmilarity_dict["similarity"] > 50:
                    hw_dict["mediumSimilarity"] += 1
                elif simmilarity_dict["similarity"] > 0:
                    hw_dict["lowSimilarity"] += 1
                else:
                    hw_dict["notSimilarity"] += 1

            hw_dict["homework_id"] = hw.id
            homeworks.append(hw_dict)

        return jsonify({
                "message": "Homeworks retrieved successfully",
                "homeworks": homeworks
            }), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Get all submissions of a homework
@tasks.route('/homework/<string:homework_id>/submissions', methods=['GET'])
def get_homework_submissions(homework_id):
    """
    """
    try:
        submissions_ref = db.collection("homework_submission")
        query_ref = submissions_ref.where(filter=FieldFilter("homework_id", "==", homework_id))
        query_ref = query_ref.get()
        submissions_sim_ref = db.collection("submssion_max_similarity")

        print("Carlos")             

        submissions = []
        for doc in query_ref:


            print("Carlos")

            max_sim = "NA"
            max_sub_ref = submissions_sim_ref.where(filter=FieldFilter("id", "==", doc.id)).get()
            if len(max_sub_ref) > 0:
                max_sim = round(max_sub_ref[0].to_dict()["similarity"], 2)

            print(f" max sim is: {max_sim}")
                
            doc_dict = doc.to_dict()

            print(doc_dict)

            sub = {
                "id": doc.id,
                "author": doc_dict["author"],
                "filename": doc_dict["file_name"],
                "similarityStatus": max_sim
            }
            submissions.append(sub)

        print(submissions)

        return jsonify({
                    "message": "Submissions retrieved successfully",
                    "submissions": submissions
                }), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Generates a distance matrix of all submissions
@tasks.route('/homework/<string:homework_id>/distance_matrix', methods=['GET'])
def get_distance_maatrix(homework_id):

    try:
        print("working on distance matrix")
        axis = []
        distance_matrix = []

        submissions_max_sim_ref = db.collection("homework_submission")
        query_ref = submissions_max_sim_ref.where(filter=FieldFilter("homework_id", "==", homework_id)).get()
        for doc in query_ref:
            sub_sim_dict = doc.to_dict()
            axis.append({
                "file_name": sub_sim_dict["file_name"],
                "file_url" : sub_sim_dict["file_url"],
                "author" : sub_sim_dict["author"],
                "id" : doc.id,
                "content": sub_sim_dict["content"]
            })
        
        
            
        for code_out in axis:
            row = []
            for code_in in axis:
                if code_out["id"] == code_in["id"]:
                    row.append(-1)
                else:
                    sim = match_files(code_out["content"], code_in["content"])
                    print(sim)
                    row.append(sim)
            distance_matrix.append(row)

        

        
        new_axis = []
        for code in axis:
            new_axis.append({
                "filename": code["file_name"],
                "author": code["author"],
                "id": code["id"],
            })
        

        return jsonify({
            "message": "Distance matrix successfully retrieved",
            "matrix": {
                    "distance_matrix": distance_matrix,
                    "axis": new_axis
            }
            
        }), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500




def post_max_similarity(submission_id, homework_id):
    """
    """
    # Create a reference to the homework collection
    submissions_ref = db.collection("homework_submission")

    submission_ref = submissions_ref.document(submission_id)

    # Fetch the document
    submission_document = submission_ref.get()
    temp_dict = submission_document.to_dict()
    submission_dict: SubmissionTable = SubmissionTable(temp_dict["author"], temp_dict["file_name"],
                                                       temp_dict["file_url"], temp_dict["fingerprint"])
    
    # Create a query against the collection to get all submissions
    query_ref = submissions_ref.where(filter=FieldFilter("homework_id", "==", homework_id))
    query_ref = query_ref.get()
    submissions = [doc for doc in query_ref]

    # Read code from storage
    submission_a_content: str = read_python_file(temp_dict["file_url"])


    max_similarity: int = 0
    submission_a: Submission = Submission(submission_document.id, submission_dict.file_name, submission_a_content, submission_dict.author)
    submission_b = None
    submission_b_dict = None

    for sub in submissions:
        temp_dict = sub.to_dict()
        current_submission: SubmissionTable = SubmissionTable(temp_dict["author"], temp_dict["file_name"],
                                                       temp_dict["file_url"], temp_dict["fingerprint"])
        similarity = match_fingerprints(submission_dict.fingerprint, current_submission.fingerprint)

        # Same submission id
        if submission_document.id == sub.id:
            continue

        if similarity > max_similarity:
            max_similarity = similarity

            # Read code from storage
            submission_b_content: str = read_python_file(temp_dict["file_url"])
            
            submission_b = Submission(sub.id, current_submission.file_name, submission_b_content, current_submission.author)
            submission_b_dict = current_submission

    if max_similarity == 0:
        return jsonify({"message": "No homeworks to compare"}), 201

   ## For Submission A, group all same matches Positions
    dict_hash_pos_a = {}

    for fp in submission_dict.fingerprint:
        if fp["hash"] not in dict_hash_pos_a:
            dict_hash_pos_a[fp["hash"]] = []

        kposition = KGramPosition(fp["position"]["lineno"],
                                      fp["position"]["col_offset"],
                                      fp["position"]["end_lineno"],
                                      fp["position"]["end_col_offset"])
        
        dict_hash_pos_a[fp["hash"]].append(kposition)

    ## For Submission B, group all same matches Positions
    dict_hash_pos_b = {}

    for fp in submission_b_dict.fingerprint:
        if fp["hash"] not in dict_hash_pos_b:
            dict_hash_pos_b[fp["hash"]] = []

        kposition = KGramPosition(fp["position"]["lineno"],
                                      fp["position"]["col_offset"],
                                      fp["position"]["end_lineno"],
                                      fp["position"]["end_col_offset"])
        
        dict_hash_pos_b[fp["hash"]].append(kposition)

    ## For Submission A, get matching kgrams from B
    matches: List[KGramHashMatch] = []

    for hash in dict_hash_pos_a:
        if hash in dict_hash_pos_b:
            kgram_match = KGramHashMatch(hash, dict_hash_pos_a[hash], dict_hash_pos_b[hash])
            matches.append(kgram_match)
            
    submission_similarity = SubmissionSimilarity(submission_document.id, max_similarity, 
                                                 submission_a, submission_b,
                                                 matches, homework_id)
    
    update_time, hw_ref = db.collection("submssion_max_similarity").add(submission_similarity.to_json())


