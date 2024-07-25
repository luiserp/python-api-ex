import spacy
spacy.prefer_gpu()

def ner_text(text):
    nlp = spacy.load("es_dep_news_trf")
    doc = nlp(text)

    entities = []
    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "start": ent.start_char,
            "end": ent.end_char,
            "label": ent.label_
        })
        
    return {
        "entities": entities,
        "model": "es_dep_news_trf"
    }    