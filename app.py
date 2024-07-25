from flask import Flask, request
from nlp.ner_text import ner_text
from nlp.sentiment import get_sentiment
from nlp.embeddings import get_embeddings
from nlp.knn_text import knn_text
from database.database import configure_database
from nlp.description import get_description

from waitress import serve
from dotenv import load_dotenv
from os import environ

load_dotenv()

app = Flask(__name__)
database = configure_database(app)

@app.route("/", methods=["GET"])
def home():
    return "Hello World"

@app.route("/nlp", methods=["POST"])
def sentiment():
    data = request.get_json()
    return get_sentiment(data["text"])
    
@app.route("/embeddings", methods=["POST"])
def embeddings():
    data = request.get_json()
    return get_embeddings(data["text"])

@app.route("/knn", methods=["POST"])
def knn():
    data = request.get_json()
    return {
        "knn": knn_text(data["text"], database),
        "text": data["text"]
    }
    
@app.route("/ner", methods=["POST"])
def ner():
    data = request.get_json()
    return {
        "ner": ner_text(data["text"]),
        "text": data["text"]
    }

@app.route("/description", methods=["POST"])
def description():
    data = request.get_json()
    return {
        "description": get_description(data["text"]),
        "text": data["text"]
    }


if __name__ == "__main__":
    host = environ.get("FLASK_HOST", "127.0.0.1")
    port = environ.get("FLASK_RUN_PORT", 5000)
    print(f"Running server on http://{host}:{port}")
    serve(app, host=host, port=port)

    
    

    
