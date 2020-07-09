# Your code here
ignored = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
   
def histogram():
    counts = {}
    with open("robin.txt") as f:
        words = f.read()
    new_string = words.lower().split()
    
    for word in new_string:
        no_ignored = ""
        for character in word:
            if character not in ignored:
               no_ignored += character
            word = no_ignored
        
        if word in counts:
            counts[word] +=1 
        elif word == "":
            break
        else:
            counts[word] = 1
            
    items = list(counts.items())

# Sort ascending by key
    items.sort(key=lambda e: (-e[1], e[0]))
    counts = (dict(items))
    
    for (string, value) in counts.items():
        max_len = len(max(string, key=len))
        print(f'{string} {" " * max_len} {"#" * value}')


print(histogram()) 
