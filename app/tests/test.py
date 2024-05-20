"""
    matcher.py

    This module contains tests match two different files.
"""
from typing import List
from app.utils.ast_node import Ast_node
from app.files.files import get_absolute_file_path
from app.utils.winnowing_lib import get_fingerprint

# Store all test files
file_paths: List[str] = get_absolute_file_path()
file_paths.sort()

def test_kgrams():
    fingerprint_0: List[Ast_node] = get_fingerprint(file_paths[0])
    print(fingerprint_0)

    

test_kgrams()

