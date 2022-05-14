import requests
import json

import emotion_test as et

def getResponse(msg):
    #getting the emotional analysis data
    emotion = et.emotion_detection()
    
    # local api call to docker hosted chatbot
    url = 'http://localhost:8080/cakechat_api/v1/actions/get_response'
    chat_data = {
        'context': [msg],
        'emotion': emotion
    }

    #getting the chat response 
    chat_response = requests.post(url, json=chat_data)
    
    #loading the json data received from the chatbot
    json_data = json.loads(chat_response.text)
    response_chat_data = json_data['response']    
    
    return(response_chat_data)

print (getResponse(msg='Today is not a good day'))