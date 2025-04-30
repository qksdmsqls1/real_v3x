#텍스트를 음성으로 변환
# text_to_speech.py

# import pyttsx3

# def speak(text):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 180)  # 말하는 속도 
#     engine.setProperty('volume', 1.0)  # 볼륨 (0.0 ~ 1.0)
#     engine.say(text)
#     engine.runAndWait()

# # 테스트용
# if __name__ == "__main__":
#     speak("어서오세요. V three X카페입니다. 주문 도와드리겠습니다.")

import os
from google.cloud import texttospeech
import playsound
import pygame

# Google 서비스 계정 키 경로 설정 (절대 경로 or 상대 경로)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "real_v3x/secrets/v3x-project-4fab2d807b9f.json"

def speak(text):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)

    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue
    
    pygame.mixer.music.unload()

# 테스트용
if __name__ == "__main__":
    speak("어서오세요. V three X 카페입니다. 주문 도와드리겠습니다.")
