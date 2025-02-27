''''
This is a setup script meant to setup you environment to run the app
This would include firing up the flask server in order to manage requests

'''

import os
import subprocess
import json
from dotenv import load_dotenv

CONFIG_PATH = "config.json"

def write_env_file(api_keys):
    with open(".env","a") as envFile:
        envFile.write('UPLOAD_FOLDER =  "media/uploaded/",\nAUDIO_FILE_PATH = "media/uploaded/uploaded_audio.wav"')
        
        for key,value in api_keys.items():
            envFile.write(f"{key} = {value}\n")

def install_requirements():
    """
    Installs the required dependencies from requirements.txt.
    """
    print("[INFO] Installing dependencies...")
    try:
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        print("[INFO] Dependencies installed successfully.")
        
    except subprocess.CalledProcessError as e:
        print("[ERROR] Failed to install dependencies.")
        raise e

def start_server():
    """
    Starts the Flask server by running app.py.
    """
    print("[INFO] Starting Flask server...")
    try:
        subprocess.run(["python", "app.py"])
        
    except KeyboardInterrupt:
        print("\n[INFO] Server stopped.")
    except Exception as e:
        print("[ERROR] Failed to start the server.")
        raise e

def main():
    """
    Main setup script logic.
    """
    print("Welcome to the Flask App Setup!\n")

    # Get user inputs for API keys
    openai_api_key = input("Please enter your OpenAI API key: ").strip() or os.getenv('OPENAI_API_KEY')
    worqhat_api_key = input("Please enter your WorqHat API key: ").strip() or os.getenv('WORQHAT_API_KEY')

    if not openai_api_key or not worqhat_api_key:
        print("[ERROR] Both API keys are required. Exiting setup.")
        return

    # Write API keys to .env file
    api_keys = {
        "OPENAI_API_KEY": openai_api_key,
        "WORQHAT_API_KEY": worqhat_api_key,
    }
    write_env_file(api_keys)
    
    
    # Loading the local environment variables
    load_dotenv()

    # Install dependencies
    install_requirements()

    # Start the server
    start_server()

if __name__ == "__main__":
    main()
