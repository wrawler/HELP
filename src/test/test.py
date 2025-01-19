import json
import os

CONFIG_PATH = "/config1.json"\
    
def write_env_file(api_keys):
    try:
        if os.path.exists(CONFIG_PATH):
            with open("config", "r") as file:
                config = json.load(file)
                
        else:
            config = {}

        config.update(api_keys)

        # Write back to the config file
        with open(CONFIG_PATH, "w") as file:
            json.dump(config, file, indent=4)
            
        print(f"[INFO] Successfully updated {CONFIG_PATH}.")
        
    except Exception as e:
        print(f"[ERROR] Failed to update {CONFIG_PATH}: {e}")
        raise
    
api_keys = {
    "OPENAI_API_KEY": "1234",
    "WORQHAT_API_KEY": "134343",
}

write_env_file(api_keys)