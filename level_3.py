station_raw = input('Station to be searched for: ').lower()
network = dict()
found = dict()
lines = ['Island Line', 'Tsuen Wan Line', 'East Rail Line', 'Kwun Tong Line', 'Tuen Ma Line']

#functions from level 1
def other(unknown):
    words = unknown.split(' ')
    for i in range(len(words)):
        x=list(words[i])
        y=x[0].upper()
        x[0]=y
        word = ''.join(x)
        words[i] = word
    final = ' '.join(words)
    return final
def hku():
    return "HKU"
if station_raw == 'hku':
    station = hku()
else:
    station = other(unknown=station_raw)

#inputing the network
for i in lines:
    with open(f'{i}.txt') as file:
        for line in file:
            line = line.strip()
            if i not in network:
                network[i] = [line]
            else:
                network[i].append(line)

#the real searching business follows
for i in network:
    if station in network[i]:
        if i not in found:
            found[i] = network[i]
#we've found all the lines with the given station

if not found:
    print("Station not found")
else:
    print(f'{station} Station found')
    lines_with_station = [i for i in found]
    lines_with_station.sort()
    for m in lines_with_station:
        print(f'{m}', end='')
        interchanges = []
        y = network[m]
        for item in y:
            for j in network:
                if j == m:
                    continue
                elif item in network[j]:
                    if item not in interchanges:
                        interchanges.append(item)
        interchanges.sort()
        for i in range(len(interchanges)):
            if len(interchanges)==1:
                print(f': {interchanges[i]}', end='')
            elif len(interchanges)>1:
                if i==0:
                    print(f': {interchanges[i]}, ', end='')
                elif i!= len(interchanges)-1:
                    print(f'{interchanges[i]}, ', end='')
                else:
                    print(f'{interchanges[i]}', end='')
        print()
