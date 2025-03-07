''' An emotion detection Flask application using embeddable Watson 
    NLP library, the app is deployed on localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector', methods=['GET'])
def emo_detector():
    ''' This function receives a statement from the HTML page and
        runs emotion detector using the emotion_detector()
        function.
        The output returned is a string with the set of emotions 
        along with their scores and the dominant emotion for the 
        provided statement.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return ( "For the given statement, the system response is "
    + ", ".join([f"'{emotion}': {score}" for emotion, score in
    response.items() if emotion != 'dominant_emotion'])
    + f" and 'sadness': {response['sadness']}."
    + "The dominant emotion is {response['dominant_emotion']}.")
@app.route("/")
def render_index_page():
    '''This function runs the render_template function
       on the HTML template, index.html
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
