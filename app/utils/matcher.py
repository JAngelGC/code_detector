"""
"""
from typing import List
from app.utils.winnowing_lib import get_fingerprint, get_hashes_fingerprint
from app.utils.ast_node import Ast_node

def match_files(file_path_1: str, file_path_2: str):
    """
    """

    # Get fingerprint of both files
    fingerprint_1: List[Ast_node] = get_fingerprint(file_path_1)
    fingerprint_2: List[Ast_node] = get_fingerprint(file_path_2)

    # Get shorter and larger fingerprint
    shorter_fingerprint, larger_fingerprint = sorted([fingerprint_1, fingerprint_2], 
                                                     key=lambda fingeprint: len(fingeprint))
    
    # Get hashes of each fingerprint
    shorter_fingerprint_hashes: List[str] = get_hashes_fingerprint(shorter_fingerprint)
    larger_fingerprint_hashes: List[str] = get_hashes_fingerprint(larger_fingerprint)

    # Loop hashes to find similir hashes
    similar_hashes: int = 0
    for hash in shorter_fingerprint_hashes:
        if hash  in larger_fingerprint_hashes:
            similar_hashes += 1
    
    # Get similarity
    similarity: float = round(similar_hashes / len(shorter_fingerprint_hashes), 2) * 100

    return similarity


