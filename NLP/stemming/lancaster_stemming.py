from nltk.stem import LancasterStemmer
lancaster =LancasterStemmer()
words =['running','runner','studies','happiness']
print("\n lancaster stemmer results:")
for w in words:
    print(w,"->",lancaster.stem(w))