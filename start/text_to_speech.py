#텍스트를 음성으로 변환
# text_to_speech.py

import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # 말하는 속도
    engine.setProperty('volume', 1.0)  # 볼륨 (0.0 ~ 1.0)
    engine.say(text)
    engine.runAndWait()

# 테스트용
if __name__ == "__main__":
    speak("안녕하세요. 무엇을 도와드릴까요?")
