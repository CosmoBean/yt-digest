import speech_recognition as sr

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        print("Listening to audio...", flush=True)
        audio = recognizer.record(source)
    try:
        print("Transcribing audio...", flush=True)
        text = recognizer.recognize_whisper(audio, "base")
        print(text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio", flush=True)
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        print("request error", flush=True)
        return f"Could not request results from Google Speech Recognition service; {e}"