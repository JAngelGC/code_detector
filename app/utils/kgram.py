from pythonparser.lexer import Token
from pythonparser import source
from typing import List

def generate_kgrams(tokens: List[Token], k: int) -> List[List[str]]:
    """
    Given a list of tokens, it returns its k-grams

    Input:
        tokens: List of tokens
        k: Size of the gram
    
    Returns:
        kgrams: List ok kgrams
    """
    kgrams: List[List[str]] = []
    for i in range(0, len(tokens) - k + 1):
        kgram = [tokens[t].kind for t in range(i, i + k)]
        kgrams.append(kgram)
    
    return kgrams


def calculate_hash(kgram: List[str], base: int = 256, prime: int = 101):
    """
    Given kgram, it calculates a hash

    Input:
        kgram: List of tokens
        base: Base 
        prime: Prime number to be mod
    
    Returns:
        hash_value: Hash of the kgram

    TODO: Update this function, think of value for each token
    """
    hash_value: int = 0
    for token in kgram:
        for char in token:
            hash_value = (hash_value * base + ord(char)) % prime

    return hash_value


def hash_kgrams(kgrams: List[List[str]]):
    """
    For kgrams, it returns a list of its hashes

    Input:
        kgrams: List of kgrams
    
    Returns:
        hashed_grams: List of kgram hashes
    """
    hashed_kgrams: List[int] = []
    for kg in kgrams:
        hashed_kgrams.append(calculate_hash(kg))

    return hashed_kgrams


def generate_windows(hashes: List[str], t: int, k: int):
    """
    Creates a list of windows of size w

    Input:
        hashes: List of kgram hashes
        t: Threshold
        k: Size of kgrams
    
    Returns:
        windows: List of the windows
    """
    w: int = t - k + 1
    windows: List[List[int]] = []
    for i in range(0, len(hashes) - w + 1):
        window: List[int] = [hashes[t] for t in range(i, i + w)]
        windows.append(window)
    
    return windows


def generate_fingerprint(windows: List[List[int]]):
    """
    Given windows of kgram hashes, it returns its fingerprint

    Input:
        windows: Windows of kgram hashes
    
    Returns:
        fp: Fingerprint of the document
    """
    fp: List[int] = []
    for window in windows:
        fp.append(min(window))
    
    return fp



