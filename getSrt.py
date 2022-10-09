import requests
from api_key import *

endpoint = "https://api.assemblyai.com/v2/transcript/r68gbe0vs8-f2ee-4662-9748-26d2b4f3736d/srt"
headers = {
    "authorization": API_KEY,
}
response = requests.get(endpoint, headers=headers)
print(response.text)
