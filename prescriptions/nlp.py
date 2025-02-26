import spacy

nlp = spacy.load("en_core_web_sm")

def extract_medications(text):
    doc = nlp(text)
    medicines = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    return medicines
