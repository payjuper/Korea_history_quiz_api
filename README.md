# 🇰🇷 Korea History GPT Quiz API

A **FastAPI-based quiz API** created during the **MS AI School 6th cohort** program.  
This project integrates **Azure Cognitive Search** and **Azure OpenAI** to generate multiple-choice quiz questions on Korean history.  
Users can request a quiz and check their answers instantly.  

---

## 🚀 Features

- **Quiz Generation**
  - Input a topic (e.g., “고구려”) and receive a GPT-generated multiple-choice quiz
  - Each quiz includes: question, 5 options (①~⑤), correct answer, and explanation
- **Answer Checking**
  - Submit an answer and get instant correctness feedback
- **RAG Workflow**
  - Azure Cognitive Search → retrieve historical context  
  - Azure OpenAI → generate question, options, answer, and explanation  

---

## 📦 Installation

    git clone https://github.com/<your-username>/korea-history-quiz-api.git
    cd korea-history-quiz-api
    pip install -r requirements.txt

Dependencies include:
- fastapi  
- uvicorn  
- openai  
- azure-search-documents  
- python-dotenv  
- pydantic  

---

## ⚙️ Usage

**1. Run the server**

    uvicorn main:app --reload

**2. Generate a quiz**  
Endpoint: `POST /generate`  

Request:
    {
      "topic": "고구려 문제 주세요"
    }

Response:
    {
      "question": "고구려를 건국한 인물은 누구인가?",
      "options": ["주몽", "이성계", "광개토대왕", "김춘추", "을지문덕"],
      "answer": "주몽",
      "explanation": "고구려는 주몽이 건국한 나라입니다."
    }

**3. Check the answer**  
Endpoint: `POST /check`  

Request:
    {
      "user_answer": "김춘추",
      "correct_answer": "주몽"
    }

Response:
    {
      "is_correct": false,
      "explanation": "정답 해설은 위 문제에 포함되어 있습니다."
    }

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

    AZURE_OPENAI_API_KEY=your_key
    AZURE_OPENAI_ENDPOINT=your_endpoint
    AZURE_OPENAI_API_VERSION=2023-05-15
    AZURE_DEPLOYMENT_NAME=your_deployment
    AZURE_SEARCH_ENDPOINT=your_search_endpoint
    AZURE_SEARCH_KEY=your_search_key
    AZURE_SEARCH_INDEX=your_index

⚠️ Never commit `.env` to GitHub. `.gitignore` already excludes it.

---

## 📊 Example Workflow

1. User sends a topic → API generates a multiple-choice quiz  
2. User submits an answer → API validates and responds with correctness + explanation  

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**.  
Use at your own risk. The author is not responsible for incorrect answers or historical inaccuracies.

---

## 📌 License

MIT License