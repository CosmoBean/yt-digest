import requests

def summarize_text(text, api_key):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Summarize the following text ignoring any sponsorship or advertising:\n\n{text}"
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        response_data = response.json()
        candidates = response_data.get("candidates", [])
        if candidates:
            content = candidates[0].get("content", {})
            parts = content.get("parts", [])
            if parts:
                summary = parts[0].get("text", "Summary not found")
                return summary
            else:
                return "Error: 'parts' field is empty or missing."
        else:
            return "Error: 'candidates' field is empty or missing."

    except requests.exceptions.RequestException as e:
        return f"HTTP Error: {e}"
    except KeyError as e:
        return f"Missing key in API response: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
