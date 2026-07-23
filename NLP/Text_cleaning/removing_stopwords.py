import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
text = "This is a sample text with some stopwords."
# Tokenize the text
tokens = word_tokenize(text)
# Get the list of stopwords
stop_words = set(stopwords.words('english'))
# Remove stopwords from the tokens
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
# Join the filtered tokens back into a string
clean_text = ' '.join(filtered_tokens)
print("Original Text:", text)
print("Clean Text:", clean_text)
