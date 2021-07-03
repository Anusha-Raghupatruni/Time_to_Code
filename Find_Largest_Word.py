def naive_longest_word(string):
    count = 0
    maximum = 0
    words = []
    word = []
    for char in string:
        if char.isalnum():
            count += 1
            word.append(char)
        else:
            if word not in words and word:
                words.append(''.join(word))
                print(words)
                print(word)
                word = []
            maximum = max(maximum,count)
            count = 0
    maximum = max(maximum,count)
    if word not in words and word:
        words.append(''.join(word))
        print(words)
        print(word)
    for item in words:
        if len(item) == maximum:
            return item
string = "fun&!! time"
#print(naive_longest_word(string))

import re

def regex(string):
    string = re.findall('\w+',string)
    print(string)
    maximum = max([len(item) for item in string])
    for item in string:
        if len(item) == maximum:
            return item
givenString = "Hello therre!!! how are you"
print(regex(givenString))

