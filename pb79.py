

with open('keylogs.txt','r') as file :
    elem = file.read()
    keys = [num for num in elem.split('\n') if num]

histo = [0]*10
for key in keys :
    for letter in key :
        histo[int(letter)] = 1


nbr_present = []
for i in range(10) :
    if histo[i] == 1 :
        nbr_present.append(i)

print(nbr_present)

hashing = {}
for number in nbr_present :
    hashing[str(number)] = []

for key in keys :
    for i in range(1,3) :
        nbr = int(key[i])
        for j in range(i) :
            if not int(key[j]) in hashing[str(nbr)] :
                hashing[str(nbr)].append(int(key[j]))

print(hashing)
