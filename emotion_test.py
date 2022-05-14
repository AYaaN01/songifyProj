import requests
import json

API_key = "497065fecemsh8b0e44e0b37b243p123e35jsnfcfa89be8d14"

url = "https://ekman-emotion-analysis.p.rapidapi.com/ekman-emotion"

payload = [
	{
		"id": "1",
		"language": "en",
		"text": "Today is not a good day"
	}
]

headers = {
	"content-type": "application/json",
	"Accept": "application/json",
	"X-RapidAPI-Host": "ekman-emotion-analysis.p.rapidapi.com",
	"X-RapidAPI-Key": API_key
}

response = requests.request("POST", url, json=payload, headers=headers)
emo_text_reply = json.loads(response.text)
disp_text = emo_text_reply[0]['predictions'][0]['prediction']

def emotion_detection ():
    return disp_text