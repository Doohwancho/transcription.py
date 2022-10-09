import requests
from api_key import *

endpoint = "https://api.assemblyai.com/v2/transcript/"

json = {
    "audio_url": "https://chess-gm-naroditsky.s3.ap-northeast-2.amazonaws.com/audio_chess.mp3",
    "language_code": "en"
}
headers = {
    "authorization": API_KEY,
    "content-type": "application/json"
}

response = requests.post(endpoint, json=json, headers=headers)

print(response.json())
