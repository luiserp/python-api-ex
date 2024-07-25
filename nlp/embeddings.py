# from sentence_transformers import SentenceTransformer
import ollama

# model_name = 'hiiamsid/sentence_similarity_spanish_es'
# model = SentenceTransformer(model_name)

model_name = 'llama3'


def get_embeddings(text):
    return {
        "text": text,
        "embeddings": ollama.embeddings(model='llama3', prompt=text)['embedding'],
        "model": model_name
    }


