import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import spacy
nlp = spacy.load("en_core_web_sm")
text="""Before an AI model or Large Language Model (LLM) 
like GPT-4 can read text,😃 it needs to convert the text into numerical IDs.
This is done by mapping each token to an integer using a predefined dictionary or vocabulary🙂"""

print("Tokenization:",text.split(text),"\n")

print("Character Tokenization:",list(text),"\n")

print("sentence_tokenize:",sent_tokenize(text),"\n" )

print("word_tokenize:",word_tokenize(text),"\n" )

print("Character Tokenization:",list(text),"\n")
print("spacy_Tokenization:", "\n")
doc=nlp(text)
tokens=[token.text for token in doc]
print(tokens)