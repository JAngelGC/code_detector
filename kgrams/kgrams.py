from lexer.lexer import Lexer
from pythonparser.lexer import Token
from pythonparser import source
from typing import List
from difflib import SequenceMatcher

def generate_kgrams(tokens: List[Token], k: int):
    kgrams = []
    for i in range(0, len(tokens) - k + 1):
        kgram = [tokens[t].kind for t in range(i, i + k)]
        kgrams.append(kgram)
    
    return kgrams

def custom_hash(s, base=256, prime=101):
    """
    """
    hash_value = 0
    for gram in s:
        for char in gram:
            hash_value = (hash_value * base + ord(char)) % prime
    return hash_value


def hash_kgrams(kgrams):
    hashed_kgrams = []
    for kg in kgrams:

        # hashed_kgram = [custom_hash(k) for k in kg]
        hashed_kgrams.append(custom_hash(kg))

    return hashed_kgrams

def generate_windows(hashes, t, k):
    w = t - k + 1
    windows = []
    for i in range(0, len(hashes) - w + 1):
        kgram = [hashes[t] for t in range(i, i + w)]
        windows.append(kgram)
    
    return windows




def generate_fingerprint(windows):
    fp = []
    for window in windows:
        fp.append(min(window))
    
    return fp




# def rabin_karp_function(tokens, k, base=256, prime=101):
#     n = len(tokens)
#     m = k # len of the k-gram
    
#     window_hash = 0
#     h = 1  # b^(m-1) % prime
    
#     # Precompute h = base^(m-1) % prime
#     for i in range(m - 1):
#         h = (h * base) % prime
    
#     results = []

#     # Compute the initial hash values
#     # print(f"len m: {m}")
#     # print(tokens)
#     for i in range(m):
#         # print(tokens[i])
#         # print(tokens[i])
#         window_hash = (base * window_hash + custom_hash(tokens[i])) % prime
#         results.append(window_hash)
    
#     for i in range(n - m + 1):
#         print(tokens[i], " -- ", custom_hash(tokens[i]))
#         # Calculate the hash for the next window
#         if i < n - m:
#             window_hash = (base * (window_hash - custom_hash(tokens[i]) * h) + custom_hash(tokens[i + m])) % prime
#             results.append(window_hash)
            
#             # Handle negative hash values
#             if window_hash < 0:
#                 window_hash += prime
    
#     return results





