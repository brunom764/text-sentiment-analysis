from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()


LABEL_MAPPING = {
    "LABEL_0": "negativo",
    "LABEL_1": "neutro",
    "LABEL_2": "positivo"
}

classifier = pipeline(
    "text-classification",
    model='./bert_sentiment_model',
    tokenizer='./bert_sentiment_model'
)

class TweetRequest(BaseModel):
    text: str

@app.post("/predict")
def predict(request: TweetRequest):
    result = classifier(request.text)[0]
    return {
        "sentiment": LABEL_MAPPING[result['label']],  
        "confidence": result['score'],
        "raw_label": result['label']  
    }