""" This module defines the api server for the amotion detector """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotions():
    text_to_analyze = request.args.get('textToAnalyze')
    resp = emotion_detector(text_to_analyze)
    return (f"For the given statement, the system response is 'anger': {resp['anger']}\
             'disgust': {resp['disgust']}, 'fear': {resp['fear']}, 'joy': {resp['joy']}\
              and 'sadness': {resp['sadness']}. The dominant emotion is {resp['dominant_emotion']}",
                 200)

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000)