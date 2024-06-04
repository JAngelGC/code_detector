"""
"""
import ast
from typing import List

class Ast_node:
    def __init__(self, hash: str, lineno: int, end_lineno: int, col_offset: int, end_col_offset: int):
        self.hash = hash
        self.lineno = lineno
        self.end_lineno = end_lineno
        self.col_offset = col_offset
        self.end_col_offset = end_col_offset
    
    def get_hash(self):
        return f"{self.hash}"
    
    def get_position(self):
        return {
            "lineno": self.lineno,
            "end_lineno": self.end_lineno,
            "col_offset": self.col_offset,
            "end_col_offset": self.end_col_offset
        }

    @staticmethod
    def get_ast(code: str):
        return ast.parse(code)


    @staticmethod
    def get_children(tree, ast_nodes) -> List['Ast_node']:

        if tree == None:
            return

        node_name = tree.__class__.__name__
        if node_name != "Module":
            current_node = Ast_node(node_name, tree.lineno, tree.end_lineno, tree.col_offset, tree.end_col_offset)
            ast_nodes.append(current_node)

        if node_name == "Constant":
            return    
        
        if hasattr(tree, "value"):
            Ast_node.get_children(tree.value, ast_nodes)

        if hasattr(tree, "elts"):
            for el in tree.elts:
                Ast_node.get_children(el, ast_nodes)

        if hasattr(tree, "args") and node_name != "FunctionDef":
            for arg in tree.args:
                Ast_node.get_children(arg, ast_nodes)

        if hasattr(tree, "ops"):
            for op in tree.ops:
                Ast_node.get_children(op, ast_nodes)

        if hasattr(tree, "test"):
            Ast_node.get_children(tree.test, ast_nodes)
        
        if hasattr(tree, "body"):
            if not isinstance(tree.body, list):
                tree.body = [tree.body]
            for node in tree.body:
                Ast_node.get_children(node, ast_nodes)

        if hasattr(tree, "handlers"):
            if not isinstance(tree.handlers, list):
                tree.handlers = [tree.handlers]
            for node in tree.handlers:
                Ast_node.get_children(node, ast_nodes)

        if hasattr(tree, "orelse"):
            if not isinstance(tree.orelse, list):
                tree.orelse = [tree.orelse]
            for node in tree.orelse:
                Ast_node.get_children(node, ast_nodes)
        
        return ast_nodes
