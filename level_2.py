#input the number of lines as n
n = int(input("Number of lines: "))

#stores the filenames to access files in given order
filenames = []

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

#taking inputs and writing them in files
for i in range(1, n+1):
    name = input(f"Name of line {i}: ").lower()
    file = open(f'{other(unknown=name)}.txt', 'w')
    filenames.append(other(unknown=name))
    count = 1
    while count!= "-1":
        station = input(f"Name of station {count} on {other(unknown=name)}: ").lower()
        if station == "-1":
            count= "-1"
            break
        else:
            if station == "hku":
                app=hku()
            else:
                app=other(unknown = station)
            count+=1
        if count==2:
            file = open(f'{other(unknown=name)}.txt', 'a')
            file.write(f'{app}')
        else:
            file = open(f'{other(unknown=name)}.txt', 'a')
            file.write(f'\n{app}')
        file.close()

#printing the outputs
for item in filenames:
    p = 0
    print(f'{item}: ', end='')
    with open(f'{item}.txt') as file:
        for line in file:
            line = line.strip()
            if p == 0:
                print(f'{line}',end='')
            else:
                print(f'<->{line}', end='')
            p += 1
    print()
#the end
