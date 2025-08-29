# service/quiz.py

from service.search import search_chunks_from_azure
from service.gpt import ask_gpt, extract_answer_and_explanation
from models.schema import QuestionResponse, AnswerRequest, AnswerResponse

def generate_quiz(topic: str) -> QuestionResponse:
    context = search_chunks_from_azure(topic)
    gpt_output = ask_gpt(topic, context)
    question, options, answer, explanation = extract_answer_and_explanation(gpt_output)

    return QuestionResponse(
        question=question,
        options=options,
        answer=answer,
        explanation=explanation
    )

def check_answer(request: AnswerRequest) -> AnswerResponse:
    is_correct = request.user_answer == request.correct_answer
    return AnswerResponse(
        is_correct=is_correct,
        explanation="정답 해설은 위 문제에 포함되어 있습니다."
    )
