import contractions

text="I'm learning NLP and it's really interesting!. I can't wait to apply it in real-world projects."
# Expand contractions in the text
expanded_text=contractions.fix(text)    
print("Original Text:",text)
print("Expanded Text:",expanded_text)