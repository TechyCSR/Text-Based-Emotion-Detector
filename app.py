# Created Date: 12 April 2024
#Emotion Detector App
#Code by @TechyCSR



from flask import Flask, render_template, request
from pydash import strings as pystr
from emotion_detection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

def map_sentiment_label(sentiment_label):
    label_mapping = {
        'P+': 'Strong Positive',
        'P': 'Positive',
        'NEU': 'Neutral',
        'N': 'Negative',
        'N+': 'Strong Negative',
        'NONE': 'Without Polarity'
    }

    return label_mapping[sentiment_label]

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    sentiment_info = emotion_detector(text_to_analyze)
    status = sentiment_info['status']['msg']

    if status != 'OK':
        escaped_status = pystr.escape(status)
        return f"Invalid text! Please try again!. Error {escaped_status}"

    sentiment_score = map_sentiment_label(sentiment_info.get('score_tag', ''))
    sentimented_entity_list = sentiment_info.get('sentimented_entity_list', [])

    formatted_response = (
        "For the given statement, the system response is:\n"
        f"General Score: {sentiment_score}\n"
    )

    for entity in sentimented_entity_list:
        entity_form = entity.get('form', '')
        entity_score = map_sentiment_label(entity.get('score_tag', ''))
        formatted_response += f"Entity: {entity_form}, Score: {entity_score}\n"

    if not sentimented_entity_list:
        formatted_response += "No sentimented entities found."

    escaped_formatted_response = pystr.escape(formatted_response)
    return escaped_formatted_response

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host= "0.0.0.0", port=2000)
