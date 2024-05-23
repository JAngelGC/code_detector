from flask import Blueprint, jsonify, request, abort
from app.utils.matcher import match_files, match_fingerprints
# from app.tests.test import test_similarity
from typing import List
from app.files.files import get_absolute_file_path
from app.utils.matcher import get_fingerprint
from app.api.misc import read_python_file
from app.utils.matcher import match_files
from app.api.firestore import db
from app.api.misc import jsonify_fingerprint
from google.cloud.firestore_v1.base_query import FieldFilter


import requests


# Store all test files
file_paths: List[str] = get_absolute_file_path()
file_paths.sort()

tasks = Blueprint('tasks', __name__)



HOMEWORK_ID = 123 # NEEDS TO CHANGE

@tasks.route('/<string:submission_id>/<int:homework_id>', methods=['GET'])
def get_submission_similarity(submission_id, homework_id):
    """
    """
    # Create a reference to the cities collection
    submissions_ref = db.collection("homework_submission")

    submission_ref = submissions_ref.document(submission_id)
        
    # Fetch the document
    submission = submission_ref.get()

    # Create a query against the collection
    query_ref = submissions_ref.where(filter=FieldFilter("homework_id", "==", HOMEWORK_ID))
    query_ref = query_ref.get()
    submissions = [doc for doc in query_ref]

    max_similarity: int = 0
    for sub in submissions:
        similarity = match_fingerprints(submission.to_dict()["fingerprint"], sub.to_dict()["fingerprint"])
        if submission.id == sub.id:
            print("SAAAAMEEEEEEEEEEEE")
            continue

        if similarity > max_similarity:
            max_similarity = similarity
    
    print(f"----------------------- {max_similarity}")


    return jsonify({
            "message": "Similarity match completed",
            "similarity": max_similarity
        }), 201
    # pass


# Create a new task
@tasks.route('/', methods=['POST'])
def post_homework():
    try:
        if not request.json:
            abort(400)
        
        file_content: str = read_python_file(request.json["file_url"])
        fingerprint = get_fingerprint(file_content)
        

        homework_sub = {
            "author": request.json["author"],
            "homework_id": HOMEWORK_ID,
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

    



