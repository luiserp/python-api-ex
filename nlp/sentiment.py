from transformers import pipeline
import torch

model_name = 'lxyuan/distilbert-base-multilingual-cased-sentiments-student'
model = pipeline(
    model=model_name,
    return_all_scores=True,
    device=0 if torch.cuda.is_available() else -1
)

def get_sentiment(text):
    return {
        "text": text,
        "sentiment": model(text)[0],
        "model": model_name
    }


