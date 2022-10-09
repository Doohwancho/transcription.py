import requests

endpoint = "https://api.assemblyai.com/v2/transcript/"

json = {
    "audio_url": "https://chess-gm-naroditsky.s3.ap-northeast-2.amazonaws.com/audio_chess.mp3",
    "language_code": "en"
}
headers = {
    "authorization": "f41535c22c8348fe808cac7291211cf7",
    "content-type": "application/json"
}

response = requests.post(endpoint, json=json, headers=headers)

print(response.json())
