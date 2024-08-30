from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def detect_emotion():
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)

    result = "For the given statement, the system response is "
    emotions = ["anger", "disgust", "fear", "joy", "sadness"]

    emotion_strings = [f"'{emotion}': {response[emotion]}" for emotion in emotions]

    result += ', '.join(emotion_strings)
    result += f". The dominant emotion is {response['dominant_emotion']}."
    return result

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
