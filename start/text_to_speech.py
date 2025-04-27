#텍스트를 음성으로 변환
# text_to_speech.py

import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)  # 말하는 속도 
    engine.setProperty('volume', 1.0)  # 볼륨 (0.0 ~ 1.0)
    engine.say(text)
    engine.runAndWait()

# 테스트용
if __name__ == "__main__":
    speak("어서오세요. V three X카페입니다. 주문 도와드리겠습니다.")
