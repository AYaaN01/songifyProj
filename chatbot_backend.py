import requests
import json
import emotion_test as et #emotion tone analysis api

def getResponse(msg):
    #getting the emotional analysis data
    #emotion = et.getEmotion(msg)
    
    # local api call to docker hosted chatbot
    url = 'http://localhost:8080/cakechat_api/v1/actions/get_response'
    chat_data = {
        'context': [msg],
        'emotion': 'joy'
    }

    #getting the chat response 
    chat_response = requests.post(url, json=chat_data)
    
    #loading the json data received from the chatbot
    json_data = json.loads(chat_response.text)
    response_chat_data = json_data['response']    
    
    return str(response_chat_data)
