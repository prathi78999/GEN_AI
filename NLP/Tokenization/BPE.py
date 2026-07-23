from transformers import GPT2Tokenizer
#BertTokenizer
text ="""NLP preprocessing transformers 
            unstructured textual data efficiency"""
gpt2_tok=GPT2Tokenizer.from_pretrained("gpt2")
gpt2_tokens=gpt2_tok.tokenize(text)
print('\n GPT-2 tokens:',gpt2_tokens)
print('GPT Ids:', gpt2_tok.encode(text))
print('vocab size of gpt2:',gpt2_tok.vocab_size)