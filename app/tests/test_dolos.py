"""
    matcher.py

    This module contains tests match two different files.
"""
from typing import List
from app.files.files import get_absolute_file_path
from app.utils.matcher import match_files
import os

# Store all test files
file_paths: List[str] = get_absolute_file_path()
file_paths.sort()

def test_similarity():
    """
    """
    similarity_dict = {}

    for file_path_i in file_paths:
        max_similarity = 0
        similarity_dict[file_path_i] = {
            "similarity": max_similarity,
            "files": []
        }

        for file_path_j in file_paths:
            if file_path_i == file_path_j:
                # print(file_path_i)
                continue

            similarity: float = match_files(read_file(file_path_i), read_file(file_path_j))
            # print(f"----- sim {similarity} and {os.path.basename(file_path_i)}  {os.path.basename(file_path_j)}")

            if similarity > max_similarity:
                max_similarity = similarity
                similarity_dict[file_path_i]["similarity"] = max_similarity
                similarity_dict[file_path_i]["files"] = [os.path.basename(file_path_j)]
                continue

            if similarity == max_similarity:
                similarity_dict[file_path_i]["similarity"] = max_similarity
                similarity_dict[file_path_i]["files"].append(os.path.basename(file_path_j))
                continue
            
            
    
    for file in similarity_dict:
        # print(f"{os.path.basename(file)} --- {similarity_dict[file]['files']} --- {similarity_dict[file]['similarity']}")
        print(f"{similarity_dict[file]['similarity']}")
        # for f in similarity_dict[file]['files']:
        #     print(f[:2], end=" - ")
        # print()


def read_file(file_path: str):
    with open(file_path, "r") as f:
        data = f.read()
    
    return data

    

test_similarity()