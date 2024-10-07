import requests
import pandas as pd
import numpy as np

def emotion_detector(text_to_analyse):

    api = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    body = {
        "raw_document" :{
            "text" : text_to_analyse
        }
    }

    response = requests.post(api, json=body, headers=header).json()
    response = response["emotionPredictions"][0]["emotion"]

    # Create a data frame
    df = pd.DataFrame(response.items(), columns=['Emotion', 'Score'])
    
    # Get dominan emotion
    max_score_index = np.argmax(df["Score"])
    dominant_emotion = df.iloc[max_score_index]["Emotion"]

    # Add to dict
    response["dominant_emotion"] = dominant_emotion
    
    return response