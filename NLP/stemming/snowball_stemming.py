from nltk.stem import SnowballStemmer
snow =SnowballStemmer("english")
words =['running','runner','studies','happiness']
print("\n snowball stemmer results:")
for w in words:
    print(w,"->",snow.stem(w))