# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
from collections import Counter


frequency = [
    'E', 'T', 'A', 'O', 'H', 'N', 
    'R', 'I', 'S', 'D', 'L', 'W', 
    'U', 'G', 'F', 'B', 'M', 'Y', 
    'C', 'P', 'K', 'V', 'Q', 'J', 
    'X', 'Z'
    ]

with open("ciphertext.txt", "r", encoding='UTF8') as f:
    words = f.read()

content_counter = Counter(filter(str.isalnum, words))
mapping = {key:value for (key,value) in zip([i[0] for i in content_counter.most_common()], frequency)}
output = ""

for letter in words:
    output_letter =  letter
    if letter in mapping.keys():
        output_letter = mapping[letter]
    output += output_letter

if __name__ == "__main__":
    print(output) 