import speech_recognition as sr
from plyer import notification

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

        with self.mic as source:
            print("Adjusting for ambient noise, please wait...")
            self.recognizer.adjust_for_ambient_noise(source)

        notification.notify(
            title="OSCAR",
            message="Ready to listen",
            timeout=3
        )
        print("Ready to listen!")

    def listen_once(self, notify=True):
        with self.mic as source:
            if notify:
                print("Try calling my name (Oscar)...")
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Didn't catch that.")
            return None
        except sr.RequestError as e:
            print(f"API error: {e}")
            return None
