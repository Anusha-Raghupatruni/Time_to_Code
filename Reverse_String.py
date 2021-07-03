def simple_reverse(string):
    new_string = []
    for i in range(len(string)-1,-1,-1):
        new_string.append(string[i])
    return ''.join(new_string)

string = "Hello"
#print(simple_reverse(string))

def swap(string,a,b):
    string = list(string)
    temp = string[a]
    string[a] = string[b]
    string[b] = temp
    return ''.join(string)
def smarter_reverse(string):
    for i in range(len(string)//2):
        string = swap(string,i,len(string)-i-1)
    return string
#print(smarter_reverse(string))
string2 = reversed(string)
print(''.join(string2))

list1 = list(string)
list1.reverse()
print(''.join(list1))

