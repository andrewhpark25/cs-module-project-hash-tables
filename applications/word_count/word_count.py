def word_count(s):
    # Your code here
    ignored = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    
    counts = dict()
    
    new_string = s.lower().split()
    
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
            
    return counts
            



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))