"""
"""
from typing import List
from app.utils.winnowing_lib import get_fingerprint, get_hashes_fingerprint
from app.utils.ast_node import Ast_node

def match_files(code_data_1: str, code_data_2: str):
    """
    """

    # Get fingerprint of both files
    fingerprint_1: List[Ast_node] = get_fingerprint(code_data_1)
    fingerprint_2: List[Ast_node] = get_fingerprint(code_data_2)

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


def match_fingerprints(fingerprint_1, fingerprint_2):
    """
    """
    shorter_fingerprint, larger_fingerprint = sorted([fingerprint_1, fingerprint_2], 
                                                     key=lambda fingeprint: len(fingeprint))
    

    # [{'position': {'lineno': 2, 'col_offset': 12, 'end_col_offset': 39, 'end_lineno': 2}, 'hash': '6092963f04594b9f6a564aa999e2830c'}, 
    #  {'position': {'lineno': 5, 'col_offset': 0, 'end_col_offset': 44, 'end_lineno': 5}, 'hash': '388d19e4e5c3b47e20c2fe19225675ff'}, 
    #  {'position': {'lineno': 5, 'col_offset': 20, 'end_col_offset': 44, 'end_lineno': 5}, 'hash': '84ec70d07869a6b1cf7cba6823c179d9'}, 
    #  {'position': {'lineno': 8, 'col_offset': 0, 'end_col_offset': 43, 'end_lineno': 8}, 'hash': 'a2155eb76da9799c1325f91f380e687d'}, 
    #  {'position': {'lineno': 9, 'col_offset': 10, 'end_col_offset': 32, 'end_lineno': 9}, 'hash': '190a9936e26fb444206aa015dbb421f1'},
    #  {'position': {'lineno': 12, 'col_offset': 0, 'end_col_offset': 49, 'end_lineno': 12}, 'hash': '388d19e4e5c3b47e20c2fe19225675ff'}, 
    #  {'position': {'lineno': 12, 'col_offset': 15, 'end_col_offset': 49, 'end_lineno': 12}, 'hash': '84ec70d07869a6b1cf7cba6823c179d9'},
    #  {'position': {'lineno': 18, 'col_offset': 4, 'end_col_offset': 18, 'end_lineno': 21}, 'hash': '0d40cd236590ab38d4925e07092e8cc0'}, 
    #  {'position': {'lineno': 19, 'col_offset': 8, 'end_col_offset': 13, 'end_lineno': 19}, 'hash': '2764545a5ea5028b650012faaae0aefa'}, 
    #  {'position': {'lineno': 21, 'col_offset': 0, 'end_col_offset': 14, 'end_lineno': 21}, 'hash': '1525ab8dfc3b30ee3924d83a85f2eec1'}, 
    #  {'position': {'lineno': 23, 'col_offset': 4, 'end_col_offset': 14, 'end_lineno': 24}, 'hash': '0d40cd236590ab38d4925e07092e8cc0'}, 
    #  {'position': {'lineno': 24, 'col_offset': 17, 'end_col_offset': 19, 'end_lineno': 24}, 'hash': '4df55dc74e6fa9b1d46ef59a38bf9ede'}]


    shorter_fingerprint_hashes = [fp["hash"] for fp in shorter_fingerprint]
    larger_fingerprint_hashes = [fp["hash"] for fp in larger_fingerprint]

    # print(shorter_fingerprint_hashes)
    # print(larger_fingerprint_hashes)
    
    # Loop hashes to find similir hashes
    similar_hashes: int = 0
    for fp in shorter_fingerprint_hashes:
        if fp  in larger_fingerprint_hashes:
            similar_hashes += 1
    
    # Get similarity
    similarity: float = round(similar_hashes / len(shorter_fingerprint_hashes), 2) * 100

    return similarity
    


