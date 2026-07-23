import nltk
from nltk.tokenize import sent_tokenize
#nltk.download('punkt')  
#nltk.download('punkt_tab')
text="""Artificial intelligence (AI) is a branch of computer science that aims to create machines that can perform tasks that typically require human intelligence. These tasks include learning, reasoning, problem-solving, perception, and language understanding.
AI has a wide range of applications across various industries, including healthcare, finance, transportation, and entertainment. In healthcare, AI can assist in diagnosing diseases, analyzing medical images, and developing personalized treatment plans.
"""
print(sent_tokenize(text))