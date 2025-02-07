


with open('words.txt', 'r') as file:
    # Read the content of the file
    content = file.read()

    # Split the content into words
    words = content.split()
    word_list = words[0].replace('"', '').split(',')
    


def count(word) :

    Sum = 0
    for letter in word :
        if  65<=ord(letter)<=91 :
            Sum += ord(letter) - 64
    return Sum


X = [i*(i+1)/2 for i in range(1,40)]

S = 0
for word in word_list :
    n = count(word)

    i = 0
    while i < len(X) and n!=X[i] :
        i += 1
    if i < len(X) :
        S += 1

print(S)