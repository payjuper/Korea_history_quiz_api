from openai import AzureOpenAI
from config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_VERSION,
    AZURE_DEPLOYMENT_NAME,
)

client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

def ask_gpt(question, context):
    messages = [
        {
            "role": "system",
            "content": (
                "너는 한국사 선생님이야. 학생에게 기출문제를 기반으로 문제를 변형해서 출제해줘.\n"
                "- 문제는 한 개만 생성해.\n"
                "- 반드시 ① ~ ⑤ 보기로 구성된 객관식 문제로 만들어줘.\n"
                "- 보기는 각각 줄바꿈해서 보여줘.\n"
                "- 마지막 줄에 반드시 다음 형식으로 포함해:\n"
                "정답: ①\n"
                "해설: ~~~ (한두 문장 설명)"
            )
        },
        {
            "role": "user",
            "content": f"다음 내용을 참고해서 한국사 문제를 만들어줘:\n\n{context}\n\n주제: {question}"
        }
    ]

    response = client.chat.completions.create(
        model=AZURE_DEPLOYMENT_NAME,
        messages=messages,
        temperature=0.4,
        max_tokens=1000
    )

    return response.choices[0].message.content


def extract_answer_and_explanation(text):
    """
    GPT 응답에서 문제, 보기, 정답, 해설을 분리하는 함수
    """
    lines = text.strip().split("\n")

    question = ""
    options = []
    answer = ""
    explanation = ""

    for line in lines:
        line = line.strip()
        if line.startswith("①") or line.startswith("②") or line.startswith("③") or line.startswith("④") or line.startswith("⑤"):
            options.append(line)
        elif line.startswith("정답:"):
            answer = line.split("정답:")[-1].strip()
        elif line.startswith("해설:"):
            explanation = line.split("해설:")[-1].strip()
        elif not line.startswith("-") and not line.startswith("문제") and not line.startswith("고르시오"):
            # 보기 이전까지는 문제 텍스트로 인식
            if not options:
                question += line + " "

    return question.strip(), options, answer, explanation.strip()
