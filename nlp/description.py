# from sentence_transformers import SentenceTransformer
import ollama

# model_name = 'hiiamsid/sentence_similarity_spanish_es'
# model = SentenceTransformer(model_name)

model_name = 'TextDescriptor'

def get_description(text):
    return {
        "description": ollama.generate(model=model_name, prompt=text)["response"],
        "model": model_name
    }


