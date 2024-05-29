from flask import Blueprint, jsonify, request, abort
from google.cloud.firestore_v1.base_query import FieldFilter
from typing import List, Dict
from app.utils.matcher import match_fingerprints, get_fingerprint
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


    max_similarity: int = 0
    submission_a: Submission = Submission(submission_document.id, submission_dict.file_name, "", submission_dict.author)
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
            submission_b = Submission(sub.id, current_submission.file_name, "", current_submission.author)
            submission_b_dict = current_submission

    if max_similarity == 0:
        return jsonify({"message": "No homeworks to compare"}), 201
    
    matches: List[KGramHashMatch] = []
    set_a = set()
    for fp in submission_dict.fingerprint:
        if fp["hash"] not in set_a:
            set_a.add(fp["hash"])
            kposition = KGramPosition(fp["position"]["lineno"],
                                      fp["position"]["end_lineno"],
                                      fp["position"]["col_offset"],
                                      fp["position"]["end_col_offset"])
            kgram_match = KGramHashMatch(fp["hash"], [kposition], [])
            matches.append(kgram_match)
        else:
            for match in matches:
                if fp["hash"] == match.hash:
                    kposition = KGramPosition(fp["position"]["lineno"],
                                      fp["position"]["end_lineno"],
                                      fp["position"]["col_offset"],
                                      fp["position"]["end_col_offset"])
                    match.submissionA.append(kposition)
    
    for fp in submission_b_dict.fingerprint:
        if fp["hash"] not in set_a:
            set_a.add(fp["hash"])
            kposition = KGramPosition(fp["position"]["lineno"],
                                      fp["position"]["end_lineno"],
                                      fp["position"]["col_offset"],
                                      fp["position"]["end_col_offset"])
            kgram_match = KGramHashMatch(fp["hash"], [], [kposition])
            matches.append(kgram_match)
        else:
            for match in matches:
                if fp["hash"] == match.hash:
                    kposition = KGramPosition(fp["position"]["lineno"],
                                      fp["position"]["end_lineno"],
                                      fp["position"]["col_offset"],
                                      fp["position"]["end_col_offset"])
                    match.submissionB.append(kposition)

            
    submission_similarity = SubmissionSimilarity(submission_document.id, max_similarity, 
                                                 submission_a, submission_b,
                                                 matches)
    
    return jsonify(submission_similarity.to_json()), 201

# Post a subbmission
@tasks.route('/submission', methods=['POST'])
def post_submission():
    try:
        if not request.json:
            abort(400)
        
        file_content: str = read_python_file(request.json["file_url"])
        fingerprint = get_fingerprint(file_content)

        homework_sub = {
            "author": request.json["author"],
            "homework_id": request.json["homework_id"],
            "file_name": request.json["file_name"],
            "file_url": request.json["file_url"],
            "fingerprint": jsonify_fingerprint(fingerprint)
        }

        update_time, hw_ref = db.collection("homework_submission").add(homework_sub)
    
        return jsonify({
            "message": "Homework submission saved successfully",
            "submission_id": hw_ref.id
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
        submissions = [doc.to_dict() for doc in query_ref]
        # print(submissions)

        return jsonify({
                    "message": "Homeworks retrieved successfully",
                    "homeworks": submissions
                }), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500




