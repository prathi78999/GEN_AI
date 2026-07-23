import spacy 
nlp=spacy.load("en_core_web_sm")
doc=nlp("Wow!! 🤩 I bought this smartphone for ₹29,999, and it's amazing")
tokens=[token.text for token in doc]
print(tokens)

