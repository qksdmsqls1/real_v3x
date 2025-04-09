# speech_to_text.py

import sounddevice as sd
import numpy as np
import whisper
import scipy.io.wavfile as wav
import tempfile
from gpt_response import get_gpt_response  # GPT 함수 불러오기
from text_to_speech import speak  # TTS 함수 불러오기

SAMPLE_RATE = 16000
DURATION = 5  # 초 단위 녹음 시간

def record_audio():
    print("🎙 음성을 녹음하세요... (5초)")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='float32')
    sd.wait()
    print("✅ 녹음 완료!")
    return audio

def save_temp_wav(audio):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, SAMPLE_RATE, (audio * 32767).astype(np.int16))
        return f.name

def transcribe(audio_path):
    model = whisper.load_model("base")  # 필요한 경우 "small", "medium"으로 변경 가능
    result = model.transcribe(audio_path, language="ko")
    return result["text"]

if __name__ == "__main__":
    audio = record_audio()
    wav_path = save_temp_wav(audio)
    text = transcribe(wav_path)
    print(f"📝 인식된 텍스트: {text}")

    # GPT에 텍스트 보내고 응답 받기
    gpt_answer = get_gpt_response(text)
    print(f"🤖 GPT 응답: {gpt_answer}")

    # 음성으로 응답 읽기
    speak(gpt_answer)
