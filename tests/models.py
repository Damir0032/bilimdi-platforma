from dataclasses import dataclass

@dataclass
class Question:
    text: str
    choice_a: str
    choice_b: str
    choice_c: str
    choice_d: str
    correct_answer: str

@dataclass
class Test:
    title: str
    questions: list[Question]

@dataclass
class Result:
    test_id: str
    user_id: str
    score: int
    total: int
    timestamp: str