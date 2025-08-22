# emotion_detection.py
import json
import requests

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse):
    """
    Returns a dict with five scores and dominant_emotion.
    If the upstream returns HTTP 400 (blank text), return the same keys with None values.
    """
    payload = {"raw_document": {"text": text_to_analyse if text_to_analyse is not None else ""}}
    response = requests.post(URL, headers=HEADERS, json=payload)

    # Required by the assignment for blank entries:
    if response.status_code == 400:
        return {
            "anger": None, "disgust": None, "fear": None,
            "joy": None, "sadness": None, "dominant_emotion": None
        }

    # Normal success path
    data = json.loads(response.text)
    emotions = data["emotionPredictions"][0]["emotion"]
    scores = {
        "anger":   emotions.get("anger", 0.0),
        "disgust": emotions.get("disgust", 0.0),
        "fear":    emotions.get("fear", 0.0),
        "joy":     emotions.get("joy", 0.0),
        "sadness": emotions.get("sadness", 0.0),
    }
    dominant = max(scores, key=scores.get)

    return {**scores, "dominant_emotion": dominant}