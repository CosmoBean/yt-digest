from flask import Blueprint, request, render_template

from app.youtube_downloader import download_audio, convert_to_wav
from app.transcription import transcribe_audio
from app.summarization import summarize_text

from config import Config

# Define a Blueprint
app_routes = Blueprint("routes", __name__)


@app_routes.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        youtube_url = request.form.get("youtube_url")
        try:
            print("in route", flush=True)
            audio_path = download_audio(youtube_url)
            wav_path = convert_to_wav(audio_path)
            transcript = transcribe_audio(wav_path)
            summary = summarize_text(transcript, Config.GEMINI_API_KEY)
            return render_template("result.html", transcript=transcript, summary=summary)
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template("index.html")
