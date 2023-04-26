import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def send_message(self, message: str=""):
    url = "https://waifu.p.rapidapi.com/path"

    querystring = {"user_id":"sample_user_id","message":message,"from_name":"Boy","to_name":"Girl","situation":"Girl loves Boy.","translate_from":"auto","translate_to":"auto"}

    payload = {}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": os.getenv("RAPID_API"),
        "X-RapidAPI-Host": "waifu.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers, params=querystring)

    return response.text
