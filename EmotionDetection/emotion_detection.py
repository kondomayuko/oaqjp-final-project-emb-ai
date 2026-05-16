# 2a_emotion_detection

import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, headers=headers, json=input_json)
    
    # Error handling for blank entries (Status Code 400)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Successful response parsing (Status Code 200)   
    elif response.status_code == 200:
        # Convert the response text into a dictionary
        formatted_response = json.loads(response.text)

        # Extract the required set of emotions
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']

        # Create a dictionary to find the dominant emotion
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        # Find the dominant emotion (the key with the highest value)
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return the output in the requested format
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        
    else:
        return {"error": f"Request failed with status code {response.status_code}"}