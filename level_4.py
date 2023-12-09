#initial inputs
origin_raw = input("Origin station: ").lower()
destination_raw = input("Destination station: ").lower()

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

#converting the raw inputs to proper formatted names
if origin_raw == "hku":
    origin = 'HKU'
else:
    origin = other(unknown=origin_raw)

if destination_raw == 'hku':
    destination = 'HKU'
else:
    destination = other(unknown=destination_raw)

#importing the sub-networks
lines = ['Island Line', 'Tsuen Wan Line', 'East Rail Line', 'Kwun Tong Line', 'Tuen Ma Line']
network = dict()
for i in lines:
    with open(f'{i}.txt') as file:
        for line in file:
            line = line.strip()
            if i not in network:
                network[i] = [line]
            else:
                network[i].append(line)

#finding lines that have the origin
lines_with_origin = []
for i in network:
    if origin in network[i]:
        lines_with_origin.append(i)
lines_with_origin.sort()

#finding lines that have the destination
lines_with_destination = []
for i in network:
    if destination in network[i]:
        lines_with_destination.append(i)
lines_with_destination.sort()

#printing the results
if len(lines_with_origin)==0 or len(lines_with_destination)==0:
    print('Station(s) not found')
else:
    #covering the case where stations are in same lines
    lines_with_origin_and_destination = []
    for i in lines_with_origin:
        if i in lines_with_destination:
            if i not in lines_with_origin_and_destination:
                lines_with_origin_and_destination.append(i)
    lines_with_origin_and_destination.sort()

    if lines_with_origin_and_destination:
        for i in lines_with_origin_and_destination:
            print(i)

    #dealing with the rest of the cases
    else:
        interchange_stations = []
        for i in lines_with_origin:
            origin_stations = network.get(i)
            for j in origin_stations:
                for k in lines_with_destination:
                    destination_stations = network.get(k)
                    if j in destination_stations:
                        if [i,k,j] not in interchange_stations:
                            interchange_stations.append([i,k,j])

        #the case of no paths or direct routes
        if not interchange_stations:
            print('More than one change or no route found')
        else:
            #arranging the interchange stations in alphabetical order
            def sort_by_third_item(element):
                return element[2]
            interchange_stations.sort(key=sort_by_third_item, reverse=False)

            for item in interchange_stations:
                origin_route = []
                origin_route.append(origin)
                origin_route.append(item[2])

                destination_route=[]
                destination_route.append(item[2])
                destination_route.append(destination)

                #the printing!!!
                #printing station name for origin
                print(f'{item[0]}: ', end='')
                for station in range(len(origin_route)):
                    if station==0:
                        print(f'{origin_route[station]}->', end='')
                    elif station==1:
                        print(f'{origin_route[station]}', end='')
                print()
                #printing station name for destination
                print(f'{item[1]}: ', end='')
                for station in range(len(destination_route)):
                    if station==0:
                        print(f'{destination_route[station]}->',end='')
                    elif station==1:
                        print(f'{destination_route[station]}', end='')
                print()
#the end
