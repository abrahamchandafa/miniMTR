name = input("Name: ").lower()

def hku():
    return "HKU"

def other():
    global name
    words = name.split(' ')
    for i in range(len(words)):
        x=list(words[i])
        y=x[0].upper()
        x[0]=y
        word = ''.join(x)
        words[i] = word
    final = ' '.join(words)
    return final

if name == "hku":
    print(f'Formatted name: {hku()}')
else:
    print(f'Formatted name: {other()}')
