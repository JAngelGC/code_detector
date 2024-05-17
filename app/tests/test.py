"""
    matcher.py

    This module contains tests match two different files.
"""
from typing import List
from app.utils.lexer import Lexer
from app.files.files import get_absolute_file_path
from app.utils.kgram import generate_kgrams, hash_kgrams, generate_windows, generate_fingerprint

# Store all test files
file_paths: List[str] = get_absolute_file_path()
file_paths.sort()

def test_kgrams():
    file_path = file_paths[0]
    print(file_path)
    tokens, buffer = Lexer.get_tokens(file_path)
    tokens = Lexer.replace_ident(tokens, buffer)

    # print(tokens)

    for to in tokens:
        print(to)

    k = 10
    kgrams = generate_kgrams(tokens, k)
    # for kg in kgrams:
        # print(kg)

    print("--------------------------")
    hashed_kgrams = hash_kgrams(kgrams)
    for kg, hkg in zip(kgrams, hashed_kgrams):
        print(kg, " -- ", hkg)
    
    print("--------------------------")
    t = 14
    windows = generate_windows(hashed_kgrams, t, k)
    for w in windows:
        print(w)

    print("-------------------------------")
    fingerprint = generate_fingerprint(windows)
    print(fingerprint)

    

test_kgrams()





# # Tests
# pairs_of_files: List[List[str]] = [
#     [file_paths[0], file_paths[1]],
#     [file_paths[2], file_paths[3]],
#     [file_paths[0], file_paths[3]],
#     [file_paths[4], file_paths[5]]
# ]

# for pair_of_files in pairs_of_files:
#     test_match_plain_text(pair_of_files[0], pair_of_files[1])
#     test_match_preprocessed_texts(pair_of_files[0], pair_of_files[1])
