"""
    matcher.py

    This module contains tests match two different files.
"""
from typing import List
from app.files.files import get_absolute_file_path
from app.utils.matcher import match_files


# Store all test files
file_paths: List[str] = get_absolute_file_path()
file_paths.sort()

def test_similarity():
    # Get similarity between files
    similarity: float = match_files(file_paths[0], file_paths[1])
    print(f"Similarity is: {similarity}%")

    return similarity
    

    

test_similarity()

