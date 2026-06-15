# Import json library to format responses
import json
# Import the requests library to handle HTTP requests
import requests

def emotion_detector(text_to_analyze):
    """
    Function to call Emotion Detection function of Watson NLP library.
    """
    # Required parameters
    url = "https://sn-watson-emotion.labs.skills.network/v1/" \
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    # Send POST request to emotion detection
    response = requests.post(url, json=input_json, headers=headers, timeout=10)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # Extract the required set of emotions
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    # Return the formatted response
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
