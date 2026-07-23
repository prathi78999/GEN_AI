from sklearn.feature_extraction.text import CountVectorizer
text =["Before an AI model or Large Language Model (LLM) like GPT-4 can read text","😃 it needs to convert the text into numerical IDs."]
vectorizer = CountVectorizer()
X =vectorizer.fit_transform(text)
print(X)
print(vectorizer.get_feature_names_out())
print(X.toarray())
