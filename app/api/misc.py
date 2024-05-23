import requests
# from app.utils.matcher import get_fingerprint
from app.utils.ast_node import Ast_node
from typing import List

def read_python_file(url_file: str):
    
    response = requests.get(url_file)

    if response.status_code == 200:
        content = response.text
        print(content)
        return content
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return None


def jsonify_fingerprint(fingerprint: List[Ast_node]):
    """
    """
    fingerprint_jsonified = [{"hash": fp.get_hash(), "position": fp.get_position()} for fp in fingerprint]

    return fingerprint_jsonified






