from typing import List
from app.utils.kgram import generate_kgrams, hash_kgrams
from app.utils.ast_node import Ast_node
import ast

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
    t = 5
    kgram_hash_windows = generate_windows(kgram_hash_index, t, k)


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


def get_fingerprint(file_path: str):
    """
    For a file_path that directs to a code, it generates its fingerprint

    Input:
        file_path: Path of the file
    
    Returns:

    """
    # Read file
    with open(file_path, "r") as f:
        data: str = f.read()

    # Get ast tree
    ast_tree: ast = Ast_node.get_ast(data)
    
    # Get ast nodes
    ast_nodes: List[Ast_node] = Ast_node.get_children(ast_tree, [])

    # Generate kgrams    
    k: int = 3
    kgrams: List[List[Ast_node]] = generate_kgrams(ast_nodes, k)

    # Hash kgrams
    hashed_kgrams: List[Ast_node] = hash_kgrams(kgrams)

    # Get fingerprint
    fingerprint: List[Ast_node] = winnowing(hashed_kgrams, k)

    return fingerprint
    
