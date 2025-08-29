# models/schema.py

from pydantic import BaseModel
from typing import List

class QuestionRequest(BaseModel):
    topic: str  # ex. "고구려 문제 주세요"

class QuestionResponse(BaseModel):
    question: str
    options: List[str]
    answer: str
    explanation: str

class AnswerRequest(BaseModel):
    user_answer: str
    correct_answer: str

class AnswerResponse(BaseModel):
    is_correct: bool
    explanation: str
