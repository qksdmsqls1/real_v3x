# 🗣️ AI 음성인식 키오스크 (Voice Assistant Kiosk)

이 프로젝트는 사용자 음성을 인식하고, 그 내용을 GPT에게 전달하여 자연스럽게 대화하는 키오스크의 기초 테스트입니다. 음성을 5초간 녹음하고, 이를 텍스트로 변환한 뒤 GPT 응답을 받아 텍스트 및 음성으로 출력합니다.

---

## 📁 구성 파일 설명

- `gpt_response.py`: GPT-3.5/4에 질문하고 응답 받는 코드
- `speech_to_text.py`: 음성 녹음 → Whisper로 텍스트 변환 → GPT → 음성 응답
- `text_to_speech.py`: 텍스트를 음성으로 변환하는 모듈

---

## 🛠️ 설치 방법

1. **Python 3.8 이상**이 설치되어 있어야 합니다.  
2. 프로젝트 루트 디렉토리에서 아래 명령어로 필요한 패키지를 설치하세요:

```bash
pip install -r requirements.txt

.env 파일을 프로젝트 폴더에 만들어 아래처럼 작성하세요:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

실행 방법
python speech_to_text.py

5초간 음성을 녹음합니다.
Whisper로 텍스트를 추출합니다.
GPT로부터 응답을 받아 출력합니다.
응답을 음성으로 읽어줍니다.


❗ 참고 사항
첫 실행 시 Whisper 모델 다운로드로 시간이 걸릴 수 있습니다.

torch 패키지는 GPU가 없어도 CPU에서 작동하지만, 느릴 수 있습니다.

sounddevice는 일부 시스템에서 추가 설정이 필요할 수 있습니다 (예: macOS 보안 설정 등).