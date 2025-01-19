from flask import Flask, request, jsonify
import os
import json
import api_handler as handler
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

WORQHAT_API_KEY = os.getenv('WORQHAT_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
AUDIO_FILE_PATH = os.getenv('AUDIO_FILE_PATH')
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')

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
    try:
        transcript = handler.speech_to_text(AUDIO_FILE_PATH, WORQHAT_API_KEY)
    except Exception as e:
        return jsonify({"Error": f"Error processing audio with WorqHat API: {str(e)}"}), 500
    
    try:
        advice = handler.ask_chatgpt(transcript, OPENAI_API_KEY)
    except Exception as e:
        return jsonify({"Error": f"Error calling OpenAI API: {str(e)}"}), 500


    response = {
        "transcript": transcript,
        "advice": advice
    }
    
    print(response)
    return jsonify(response)

if __name__ == '__main__':
    app.run( debug = True )
