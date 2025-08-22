"""Flask web app exposing /emotionDetector and home routes for emotion detection."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

ERROR_MESSAGE = "Invalid text! Please try again!"


def _format_message(result: dict) -> str:
    """Return the required formatted sentence from an emotion result dict."""
    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


@app.route("/", methods=["GET"])
def home() -> str:
    """Render the provided index.html page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route() -> tuple[str, int]:
    """Run emotion detection for ?textToAnalyze=... and return a formatted message."""
    text = request.args.get("textToAnalyze", "")
    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return ERROR_MESSAGE, 400

    return _format_message(result), 200


if __name__ == "__main__":
    app.run(debug=True)
