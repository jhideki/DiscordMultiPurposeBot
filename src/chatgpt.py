import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def send_message(message):
    url = "https://openai80.p.rapidapi.com/chat/completions"
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": os.getenv("RAPID_API"),
        "X-RapidAPI-Host": "openai80.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    json_data = json.loads(response.text)
    if 'choices' in json_data and len(json_data['choices']) > 0:
        content = json_data['choices'][0]['message']['content']
        return content
    else:
        return None
