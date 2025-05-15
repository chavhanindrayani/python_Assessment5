#3.	Replace all occurrences of 'cat' with 'dog'.
#	Task: Write a regex to replace every occurrence of the word 'cat' with 'dog' in a given text.
#	Input: "The cat is cute. The cat is playing."
#	Expected Output: "The dog is cute. The dog is playing."

import re
def replace_cat_with_dog(text):
    return re.sub(r'cat', 'dog',text)

sentence = "the cat is cute. the cat is playing."
replace = replace_cat_with_dog(sentence)
print(replace)