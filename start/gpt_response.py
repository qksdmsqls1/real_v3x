# gpt_response.py

import os
from openai import OpenAI
from dotenv import load_dotenv

# .env 파일에서 API 키 불러오기
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  # ← 여기 변수명 주의! .env에서 이 이름으로 불러와야 해

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=api_key)

# 대화 기록을 저장하는 리스트
messages = [
    {"role": "system", "content": "당신은 친절한 키오스크 안내원입니다."}
]

def get_gpt_response(user_input):
    # 사용자의 발화를 messages에 추가
    messages.append({"role": "user", "content": user_input})

    # GPT에 전체 대화 히스토리 보내기
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    assistant_reply = response.choices[0].message.content

    # GPT의 답변도 messages에 추가
    messages.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply

if __name__ == "__main__":
    print("💬 대화를 시작하세요! (끝이라고 입력하면 종료)")
    try:
        while True:
            user_input = input("👤 나: ")
            if user_input.strip().lower() in ["끝", "종료", "그만"]:
                print("👋 대화를 종료합니다!")
                break
            answer = get_gpt_response(user_input)
            print("🤖 GPT:", answer)

    except KeyboardInterrupt:
        print("\n👋 [Ctrl+C] 감지: 프로그램 정상 종료합니다.")
