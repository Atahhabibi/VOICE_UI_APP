# test_voice.py
from speech_engine import SpeechManager
import time

speech = SpeechManager()
speech.speak("Testing speech. You should hear this message.")
time.sleep(4)
speech.stop()
