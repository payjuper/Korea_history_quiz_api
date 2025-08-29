# main.py

from fastapi import FastAPI
from models.schema import QuestionRequest, QuestionResponse, AnswerRequest, AnswerResponse
from service.quiz import generate_quiz, check_answer

app = FastAPI()

@app.post("/generate", response_model=QuestionResponse)
def generate_question(request: QuestionRequest):
    return generate_quiz(request.topic)

@app.post("/check", response_model=AnswerResponse)
def check_user_answer(request: AnswerRequest):
    return check_answer(request)
