
PATH_NAMES = "names.txt"

with open(PATH_NAMES) as file :
    elem = file.read()
    names = elem.split(',')

names =  sorted(names)
names = sorted([name.strip('"\n') for name in names])


def score(name) :
    S = 0
    for letter in name :
        S += ord(letter) - 64
    return S

print(score(names[937]))

S = 0
for (index,name) in enumerate(names) :

    S += score(name)*(index+1)
    if name == "COLIN" :
        print(score(name)*(index+1))

print (S)