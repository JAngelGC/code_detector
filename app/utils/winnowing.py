from typing import List
from app.utils.lexer import Lexer
from app.utils.kgram import generate_kgrams, hash_kgrams, generate_windows, generate_fingerprint
from pythonparser.lexer import Token

def winnowing(file_path: str):
    """
    For a file_path, 
    """

    print(file_path)



    tokens, buffer = Lexer.get_tokens(file_path)
    tokens = Lexer.replace_ident(tokens, buffer)

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






