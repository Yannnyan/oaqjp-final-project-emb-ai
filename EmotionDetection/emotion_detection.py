import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { 'raw_document': {'text': text_to_analyse}}
    resp = requests.post(url,json=body,headers=headers)
    formatted_response = json.loads(resp.text)
    emotions: dict = formatted_response['emotionPredictions'][0]['emotion']
    emotions['dominant_emotion'] = max(zip(emotions.values(),emotions.keys()))[1]
    return emotions