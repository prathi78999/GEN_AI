import re
import nltk #type: ignore
import string
from nltk.corpus import stopwords #type: ignore
from nltk.tokenize import word_tokenize #type: ignore
nltk.download('punkt') #type: ignore
nltk.download('punkt_tab') #type: ignore
nltk.download('stopwords') #type: ignore

#lowercasing
text ="""Hello!!! My name is Sam.
Visit https://openai.com
Email: sam@gmail.com
I have 2 laptops 😊."""
lower_text =text.lower()
print(lower_text)

cleaning_text=re.sub(r'\d+', '', text)
print(cleaning_text,"\n")

translator =str.maketrans('','',string.punctuation)
clean_text=text.translate(translator)
print(clean_text,"\n")

token =word_tokenize(text)
stop_word =set(stopwords.words('english'))
filtered_tokens = [word for word in token if word.lower() not in stop_words]
clean_Text=" ".join(filtered_tokens)
print(clean_Text,"\n")

text =re.sub(r'https?://\S+|www\.\S+','',text)
text =re.sub(r'\S+@\S+','',text)
print(text,"\n")