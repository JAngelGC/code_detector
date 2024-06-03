from typing import List
from app.utils.kgram import generate_kgrams, hash_kgrams
from app.utils.ast_node import Ast_node
import ast

K = 5
T = 5

def winnowing(kgram_hashList: List[Ast_node], k: int):
    """
    For kgrams, it returns a list of its hashes

    Input:
        kgrams: List of kgrams
    
    Returns:
        hashed_grams: List of kgram hashes
    """
    # Map hash index position
    kgram_hash_index = [{'hash': kgram_hash, 'idx': idx} for idx, kgram_hash in enumerate(kgram_hashList)]

    # Generate windows
    kgram_hash_windows = generate_windows(kgram_hash_index, T, k)


    # Get fingerprint
    fingerPrint_index = set()
    fingerPrint = []
    for window in kgram_hash_windows:
        sorted_window = sorted(window, key=lambda k_gram_hash: k_gram_hash["hash"].get_hash())
        min_kgram_hash = sorted_window[0]['hash'].get_hash()

        for k_gram_hash in sorted_window:
            if k_gram_hash['hash'].get_hash() != min_kgram_hash:
                break

            if k_gram_hash['idx'] not in fingerPrint_index:
                fingerPrint.append(k_gram_hash['hash'])
                fingerPrint_index.add(k_gram_hash['idx'])

    return fingerPrint


def generate_windows(hashes: List[dict], t: int, k: int):
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


def get_fingerprint(data: str) -> List[Ast_node]:
    """
    For a file_path that directs to a code, it generates its fingerprint

    Input:
        file_path: Path of the file
    
    Returns:

    """
    # Read file
    # with open(data, "r") as f:
    #     data: str = f.read()

    # Get ast tree
    ast_tree: ast = Ast_node.get_ast(data)

    #print(ast.dump(ast_tree, include_attributes=True, indent="\t"))
    #print(ast_tree.body[3].lineno)
    
    # Get ast nodes
    ast_nodes: List[Ast_node] = Ast_node.get_children(ast_tree, [])

    # Generate kgrams    
    kgrams: List[List[Ast_node]] = generate_kgrams(ast_nodes, K)

    # Hash kgrams
    hashed_kgrams: List[Ast_node] = hash_kgrams(kgrams)

    # Get fingerprint
    fingerprint: List[Ast_node] = winnowing(hashed_kgrams, K)

    return fingerprint


def get_hashes_fingerprint(fingerprint: List[Ast_node]) -> List[str]:
    """
    Given a fingerprint of Ast_node's, it return an array
    of its hashes.

    Input:
        fingerprint: List of Ast_nodes
    
    Returns:
        list_hashes: List of hashes
    """
    list_hashes: List[str] = [fp.get_hash() for fp in fingerprint]
    return list_hashes
    