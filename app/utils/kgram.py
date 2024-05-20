"""

"""

from app.utils.ast_node import Ast_node
from typing import List
import hashlib


def generate_kgrams(tokens: List[Ast_node], k: int) -> List[List[str]]:
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
        kgram = [tokens[t] for t in range(i, i + k)]
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


def hash_kgrams(kgrams: List[List[Ast_node]]) -> List[Ast_node]:
    """
    For kgrams, it returns a list of hashed Ast_nodes

    Input:
        kgrams: List of list of AST_nodes
    
    Returns:
        hashed_grams: List of hashed AST_nodes
    """
    hashed_kgrams: List[Ast_node] = []
    for kgram in kgrams:

        # To store start and end position of the kgram
        lineno: int = 0
        end_lineno: int = 0
        col_offset: int = 0
        end_col_offset: int = 0

        # Used to create the hash of the kgram
        node_names: List[str] = []

        for i in range(len(kgram)):
            if i == 0:
                # First element of kgram
                lineno = kgram[i].lineno
                end_lineno = kgram[i].end_lineno
            if i == len(kgram) - 1:
                # Last element of kgram
                col_offset = kgram[i].col_offset
                end_col_offset = kgram[i].end_col_offset
            
            node_names.append(kgram[i].hash)

        
        ngram_str: str = ' '.join(node_names)
        hash_val: str = hashlib.md5(ngram_str.encode()).hexdigest()
        node_hash: Ast_node = Ast_node(hash_val, lineno, end_lineno, 
                                       col_offset, end_col_offset)
        hashed_kgrams.append(node_hash)

    return hashed_kgrams


