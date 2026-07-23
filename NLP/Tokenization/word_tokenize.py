#Word level tokenization using split() method
text="My name is 1 pratheeksha!!!" #type:ignore
print(text.split())
#split() method cannot handle punctuations,numbers,emojis
#using nltk word_tokenize()
import nltk
from nltk.tokenize import word_tokenize

#nltk.download('punkt')
#nltk.download('punkt_tab')

text="""Wow!! 🤩 I bought this smartphone
for ₹29,999, and it's amazing! 📱 The battery lasts only 6hours. 
😕Thanks @MobileHub! Visit https://www.mobilehub.com.
I'd definitely buy again! #HappyCustomer"""
print(word_tokenize(text))