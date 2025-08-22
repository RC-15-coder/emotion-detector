from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    # Even if missing/blank, we still pass it through to emotion_detector
    text = request.args.get("textToAnalyze", "")

    result = emotion_detector(text)  # returns dict with possible None values

    # Assignment requirement: if dominant_emotion is None, show this message
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    msg = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return msg, 200

if __name__ == "__main__":
    app.run(debug=True)
