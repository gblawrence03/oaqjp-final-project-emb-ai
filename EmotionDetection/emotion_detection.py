import requests
import json

def emotion_detector(text_to_analyse):
    url = ("https://sn-watson-emotion.labs.skills.network/v1/watson."
           "runtime.nlp.v1/NlpService/EmotionPredict")  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=header, json=input_json)

    if response.status_code == 400:
        emotions = ["anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"]
        return dict.fromkeys(emotions, None)

    response_formatted = json.loads(response.text)
    emotions = response_formatted["emotionPredictions"][0]["emotion"]
    emotions["dominant_emotion"] = max(emotions, key=lambda key: emotions[key])
    return emotions
