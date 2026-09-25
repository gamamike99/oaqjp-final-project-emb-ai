"""Flask server for the emotion detection application."""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the application home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """Process text and return the detected emotions."""
    data = request.get_json()
    text_to_analyse = data.get("text", "")

    if not text_to_analyse.strip():
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyse)

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
