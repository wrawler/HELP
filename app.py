from flask import Flask, request, jsonify
import os
import json
import api_handler as handler
import subprocess
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

WORQHAT_API_KEY = os.getenv('WORQHAT_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
AUDIO_FILE_PATH = ""
UPLOAD_FOLDER = ""
    
with open("config.json") as config_File:
    config = json.load(config_File)
    AUDIO_FILE_PATH = config['AUDIO_FILE_PATH']
    UPLOAD_FOLDER = config["UPLOAD_FOLDER"]

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Route to process the audio
@app.route('/process-audio', methods = ['POST'])
def process_audio():
    if 'audio' not in request.files:
        return jsonify({"Error": "No audio file provided."})

    # Save the audio file to the local system
    audio_file = request.files['audio']
    audio_file.save(AUDIO_FILE_PATH)

    # Sending API requests to WorqHat and OpenAI in order
    transcript = handler.speech_to_text(AUDIO_FILE_PATH,WORQHAT_API_KEY)
    advice = handler.ask_chatgpt(transcript,OPENAI_API_KEY)

    response = {
        "transcript": transcript,
        "advice": advice
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run( debug = True )
