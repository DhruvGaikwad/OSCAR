from duckduckgo_search import DDGS
from speech_recog import SpeechRecognizer
import webbrowser
import time
from plyer import notification

close = ("terminate", "termina")
search = ("search", "google")
recognizer = SpeechRecognizer()#IMPORTANT

print("Oscar is listening... Say 'hey oscar' to wake me up.")

while True:
    heard = recognizer.listen_once()
    if heard is None:
        continue

    heardl = heard.lower()

    if heardl in close:
        notification.notify(
            title="OSCAR",
            message="BYEZ",
            timeout=5  # seconds
        )
        time.sleep(3)
        break

    if "oscar" in heardl:
        notification.notify(
            title="OSCAR",
            message="Yes? I'm listening...",
            timeout=2
        )
        time.sleep(2)  # Allow notification to show fully
        print("Yes? I'm listening...")

        query = recognizer.listen_once()
        if query:
            with DDGS() as ddgs:
                results = ddgs.text(query, max_results=5)
                if results:
                    webbrowser.open(results[0]["href"])

    print("\nOscar is listening again...")
