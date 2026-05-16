"""
Emotion Detection Server

This module initiates a Flask web application that routes user input to 
the EmotionDetection package and returns a formatted string of the 
detected emotions and the dominant emotion.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the user provided text for emotions and return the result.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass the text to the emotion_predictor function and store the response
    response = emotion_detector(text_to_analyze)

    # Error handling: If the dominant_emotion is None, return the error message
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
    # Format the output string exactly as requested
    formatted_response = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    
    return formatted_response

@app.route("/")
def render_index_page():
    """
    Render the main application page over the Flask channel.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)