import re
text = "This is a sample text with numbers 123 and 4567."
# Remove numbers from the text  
clean_text=re.sub(r'\d+', '', text)
print("Original Text:", text)
print("Text after removing numbers:", clean_text)