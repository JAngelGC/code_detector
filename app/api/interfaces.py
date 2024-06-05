from typing import List

class Submission():
    def __init__(self, id: str, filename: str, content: str, author: str):
        self.id = id
        self.filename = filename
        self.content = content
        self.author = author

    def to_json(self):
        return {
            "id": self.id,
            "filename": self.filename,
            "content": self.content,
            "author": self.author,
        }

    

class KGramPosition():
    def __init__(self, startLine: str, startCol: str, endLine: str, endCol: str):
        self.startLine = startLine
        self.startCol = startCol
        self.endLine = endLine
        self.endCol = endCol

    def to_json(self):
        return {
            "startLine": self.startLine,
            "startCol": self.startCol,
            "endLine": self.endLine,
            "endCol": self.endCol,
        }



class KGramHashMatch():
    def __init__(self, hash: str, submissionA: List[KGramPosition], submissionB: List[KGramPosition]):
        self.hash = hash
        self.submissionA = submissionA
        self.submissionB = submissionB
    
    def to_json(self):
        subA = [sub.to_json() for sub in self.submissionA]
        subB = [sub.to_json() for sub in self.submissionB]

        return {
            "hash": self.hash,
            "submissionA": subA,
            "submissionB": subB,
        }


class SubmissionSimilarity():
    def __init__(self, id: str, homeworkId: str, similarity: int, submissionA: Submission, submissionB: Submission, matches: List[KGramHashMatch]):
        self.id = id
        self.similarity = similarity
        self.submissionA = submissionA
        self.submissionB = submissionB
        self.matches = matches
        self.homeworkId = homeworkId
    
    def to_json(self):
        matches_ = [match.to_json() for match in self.matches]

        return {
            "id": self.id,
            "similarity": self.similarity,
            "submissionA": self.submissionA.to_json(),
            "submissionB": self.submissionB.to_json(),
            "matches": matches_,
            "homeworkId": self.homeworkId
        }



class Position():
    def __init__(self, lineno: int, end_lineno: int, col_offset: int, end_col_offset: int):
        self.lineno = lineno
        self.end_lineno = end_lineno
        self.col_offset = col_offset
        self.end_col_offset = end_col_offset


class FingerprintElement():
    def __init__(self, hash: str, position: Position):
        self.hash = hash
        self.position = position


class SubmissionTable():
    def __init__(self, author: str, file_name: str, file_url: str, fingerprint: List[FingerprintElement]):
        self.author = author
        self.file_name = file_name
        self.file_url = file_url
        self.fingerprint = fingerprint



