import gensim.downloader as api
import numpy as np
#Load the pre-trained word embedding model
model = api.load("glove-wiki-gigaword-100")  # You
text ="Machine learning is amazing"
#preprocess the text
words =[word for word in text.lower().split() if word in model.key_to_index]
if words:
    vector =np.mean([model[word] for word in words], axis=0)
    print("Vector shape:", vector.shape)
    print("Vector [first 20 dimentions]:", vector[:20])
else:
    print("No words from the text are in the model's vocabulary.")