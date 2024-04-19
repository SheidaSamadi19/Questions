# Authors: Sheida Samadi , Baran Farrokhian

# Library 
import string

# Function
# This function recieves the text, splits the words and count them and then shows how many words you used
def count_words(text):
    words = text.split()
    return len(words)

# Input
# It recieves the text
content = input("Please enter your text :")

# It declares the Function
num_words = count_words(content)
    
print("Words : ", num_words)


