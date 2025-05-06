import pyttsx3
import threading

class SpeechManager:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.lock = threading.Lock()

    def speak(self, message):
        def _speak():
            with self.lock:
                self.engine.say(message)
                self.engine.runAndWait()
        threading.Thread(target=_speak).start()

    def stop(self):
        with self.lock:
            self.engine.stop()
