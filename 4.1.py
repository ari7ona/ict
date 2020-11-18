def reverselu(a, b):
    keys = []
    for i,j in a.items():
        if j == b:
            keys.append(i)
    return keys
dict = {'Arizona':48, 'Louisiana':18}
print(reverselu(dict, 48))
print(reverselu(dict, 18))