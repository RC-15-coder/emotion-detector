from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    # This loads the provided templates/index.html (no edits required)
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Expects ?textToAnalyze=... on the query string.
    Returns: "For the given statement, the system response is 'anger': X, 'disgust': Y,
              'fear': Z, 'joy': A and 'sadness': B. The dominant emotion is D."
    """
    text = request.args.get("textToAnalyze")
    if not text or not text.strip():
        # Keep it simple (you’ll add richer errors in Task 7)
        return "Invalid input! Please provide ?textToAnalyze=...", 400

    result = emotion_detector(text)  # dict from Task 3

    # Build the exact sentence format shown in the instructions:
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
    # Default is localhost:5000
    app.run(debug=True)
