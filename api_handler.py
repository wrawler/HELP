import requests
from openai import OpenAI

def speech_to_text(audio_file_path,api_key):
    url = "https://api.worqhat.com/api/ai/speech-text"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    # Open the audio file in binary mode
    with open(audio_file_path, 'rb') as audio_file:
        files = {
            "audio": audio_file,
        }
        
        payload = {
            "language": "hi",  # Specify the language of the audio (e.g., English)
        }

        try:
            # Send a POST request to the API
            response = requests.post(url, headers=headers, files=files, data=payload)

            # Check if the request was successful
            response.raise_for_status()

            # Parse the response data
            transcript = response.json().response_data['data']['text']
            return transcript

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")

        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")

        except ValueError as json_err:
            print(f"JSON decode error: {json_err}")

def ask_chatgpt(transcript,api_key):
    client = OpenAI(api_key = api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an emergency operator. Your task is to take transcript and judge what type of emergency the person is going through. After that you need to suggest them, the proper hotline number available in India. You also need to provide basic steps that could be taken during the specific emergency or calamity. The transcript could be different languages (mainly indian languages) and you have to determine keeping this in mind. Keep this in brief, so that reponses can be received faster. Give responses in English"},

            {
                "role": "user",
                "content": transcript
            }
        ]
    )

    advice = response.choices[0].message.content
    return advice