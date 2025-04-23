# gpt_response.py

import os
from openai import OpenAI
from dotenv import load_dotenv

# .env 파일에서 API 키 불러오기
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  # ← 여기 변수명 주의! .env에서 이 이름으로 불러와야 해

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=api_key)

# GPT에게 질문 보내는 함수
def get_gpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # 또는 "gpt-4"
        messages=[
            {"role": "system", "content": "당신은 친절한 키오스크 안내원입니다."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# 테스트용 실행
if __name__ == "__main__":
    user_input = input("사용자 질문을 입력하세요.: ")
    answer = get_gpt_response(user_input)
    print("🧠 GPT 응답:", answer)
