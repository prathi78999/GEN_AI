import string

text ="Hello Welcome , to NLP. How are you?"

translator =str.maketrans('','',string.punctuation)
clean_text= text.translate(translator)

print("Original Text",text)
print("Without Punctuation",clean_text)