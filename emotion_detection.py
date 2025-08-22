# emotion_detection.py
import json
import requests

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse):
    """
    Calls the Watson NLP EmotionPredict endpoint and returns a dict:
    {
      'anger': float, 'disgust': float, 'fear': float,
      'joy': float, 'sadness': float, 'dominant_emotion': str
    }
    """
    payload = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(URL, headers=HEADERS, json=payload)  # spec: use response.text
    data = json.loads(response.text)

    # Navigate to the emotion scores
    emotions = data["emotionPredictions"][0]["emotion"]
    anger   = emotions.get("anger",   0.0)
    disgust = emotions.get("disgust", 0.0)
    fear    = emotions.get("fear",    0.0)
    joy     = emotions.get("joy",     0.0)
    sadness = emotions.get("sadness", 0.0)

    scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
    }
    dominant = max(scores, key=scores.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant,
    }
