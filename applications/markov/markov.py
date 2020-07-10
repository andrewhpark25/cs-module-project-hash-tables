import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
# TODO: construct 5 random sentences
# Your code here

new = words.split()

def markov(arr):
    for i in range(len(arr) - 1):
        yield (arr[i], arr[i + 1])
        
pairs = markov(new)

word_dict = dict()

for word, word2 in pairs:
    if word in word_dict.keys():
        word_dict[word].append(word2)
    else:
        word_dict[word] = [word2]
        
first_word = random.choice(new)

last_word = random.choice(new)

while first_word.islower() and first_word[0] != '"':
    first_word = random.choice(new)
while last_word[-1] not in ['.', '!', '?']:
    last_word = random.choice(new)
    
firstword = [first_word]
lword = [last_word]

n_words = 50

for i in range(n_words):
    firstword.append(random.choice(word_dict[firstword[-1]]))
    
print(' '.join(firstword + lword))


