# **YouTube to Text and Summarization App**

A Flask-based web application that converts YouTube videos into text files using speech recognition and provides a concise summary of the transcript using Gemini APIs.

---

## **Features**
- Download audio from YouTube videos.
- Convert the audio to text using `SpeechRecognition`.
- Cleans up the transcript for any sponsors/ads content/
- Summarize the transcript using Gemini APIs.
- Simple web interface for easy interaction.
---

## **Running Locally**
- use python 3.10, other versions might be incompatible with pyTorch libraries
- install all the dependencies from requirements.txt
- make a .env file from the .env.sample, and place your gemini API key there
- run app.py.
- open localhost:5000, paste the link and simplify your yt videos!
---

## **Technologies Used**
- **Python**: Backend logic.
- **Flask**: Web framework for the application.
- **pytube**: To download audio from YouTube videos.
- **pydub**: For audio conversion.
- **SpeechRecognition**: For speech-to-text processing.
- **Gemini API**: For text summarization & cleaning.
- **HTML/CSS**: For the web interface.

---

## **Project Structure**

```plaintext
youtube-to-text/
├── app/
│   ├── __init__.py           # Initializes the Flask app
│   ├── routes.py             # Contains the Flask routes (as Blueprints)
│   ├── youtube_downloader.py # Logic for downloading YouTube audio
│   ├── transcription.py      # Handles audio-to-text conversion
│   ├── summarization.py      # Calls Gemini API for text summarization
│   └── templates/            # HTML templates for the web UI
├── requirements.txt          # Python dependencies
├── config.py                 # Configuration settings (e.g., API keys)
├── app.py                    # Entry point for running the Flask app
├── README.md                 # Project documentation
├── .env.sample               # Sample env file (put your API key here)
└── .gitignore                # Files to ignore in version control
