arr = ['a', 'o', 'y', 'e', 'u', 'i']
inp = input().lower()
a = ""
for i in range(len(inp)):
    if inp[i] not in arr:
        a += "."
        a += inp[i]
print(a)