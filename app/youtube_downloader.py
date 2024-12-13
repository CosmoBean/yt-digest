import yt_dlp
import os
from pydub import AudioSegment


def download_audio(youtube_url, output_path="downloads"):
    """
    Downloads audio from a YouTube video and extracts its title and thumbnail.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'no_warnings': True,
    }

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(youtube_url, download=True)

            # Extract details
            video_title = info_dict.get('title', 'Unknown Title')
            thumbnail_url = info_dict.get('thumbnail', None)

            # Get the audio file path
            if 'requested_downloads' in info_dict and info_dict['requested_downloads']:
                audio_file = info_dict['requested_downloads'][0]['filepath']
            else:
                audio_file = ydl.prepare_filename(info_dict)
                base, ext = os.path.splitext(audio_file)
                audio_file = base + '.mp3'

            if not os.path.isfile(audio_file):
                print(f"Expected audio file not found: {audio_file}")
                return None, video_title, thumbnail_url

            print(f"Audio downloaded to {audio_file}")
            return audio_file, video_title, thumbnail_url

        except yt_dlp.utils.DownloadError as e:
            print(f"yt-dlp encountered an error: {e}")
            return None, None, None

def sanitize_filename(name):
    """
    Sanitize the filename by removing or replacing invalid characters.
    """
    import string
    valid_chars = f"-_.() {string.ascii_letters}{string.digits}"
    sanitized = ''.join(c for c in name if c in valid_chars)
    return sanitized


def convert_to_wav(input_audio_path, output_path="downloads"):
    try:
        base_name = os.path.splitext(os.path.basename(input_audio_path))[0]
        sanitized_title = sanitize_filename(base_name)
        wav_path = os.path.join(output_path, f"{sanitized_title}.wav")
        audio = AudioSegment.from_file(input_audio_path)
        audio.export(wav_path, format="wav")
        print(f"Audio converted to WAV at {wav_path}")
        return wav_path
    except FileNotFoundError:
        print(f"Input audio file not found: {input_audio_path}")
    except Exception as e:
        print(f"Error converting to WAV: {e}")

