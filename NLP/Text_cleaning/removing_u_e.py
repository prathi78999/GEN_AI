import re
text ="""
visit https://www.example.com for more information.
Contact us at info@example.com
"""
# Remove URLs and email addresses from the text
clean_text = re.sub(r'https?://\S+|www\.S+','', text)

clean_text = re.sub(r'\S+@\S+', '', clean_text)
print("Original Text:", text)
print("Clean Text:", clean_text)