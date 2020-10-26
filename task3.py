#ex1
arr = ['a', 'o', 'y', 'e', 'u', 'i']
inp = input().lower()
a = ""
for i in range(len(inp)):
    if inp[i] not in arr:
        a += "."
        a += inp[i]
print(a)

#ex2
import sys
inp = sys.stdin.readline().strip().split("+")
inp.sort()
print ("+".join(inp))

#ex3
import sys
inputs = sys.stdin.readline().strip()
print (inputs[0].upper() + inputs[1:])

#ex4
inp = list(input())
cnt = 1
for num in range(len(inp)):
    if num != len(inp) - 1:
        if inp[num] == inp[num + 1]:
            cnt += 1
        if cnt >= 7:
            break
        else:
            if cnt >= 7:
                break
            else:
                cnt = 1
    else:
        if cnt >= 7:
            print("YES")
        else:
            print("NO")
            
#ex5
import sys
inputs = sys.stdin.readline().strip()
distinctN = ""
for i in range(len(inputs)):
    char = inputs[i]
    if char not in distinctN:
        distinctN = distinctN + char
if len(distinctN) % 2 == 0:
    print ("CHAT WITH HER!")
else:
    print ("IGNORE HIM!")

#ex6
inp = input()
l = 0
u = 0
for i in inp:
    if i == i.lower(): l += 1
    else: u += 1
if u <= l:
    print(inp.lower())
else:
    print(inp.upper())

#ex7
import re
s = input()
x = re.findall("[a-zA-Z]", s)
if len(set(x)) > 26:
    print("YES")
else:
    print("NO")
    
#ex8
n = input()
t = input()
if t == n[::-1]:
    print("YES")
else:
    print("NO")
    
#ex9
import re
s = input()
a = re.findall("A",s)
b = re.findall("D",s)
if len(a) > len(b):
    print('Anton')
elif len(a) < len(b):
    print('Danik')
else:
    print('Friendship')
  
#ex10
s = input()
s = s.lower()
print(s[0].upper(),end='' + s[1:])

#ex11
import re
n = int(input())
s = input()
z = re.findall('z', s)
e = re.findall('e', s)
r = re.findall('r', s)
o = re.findall('o', s)
n = re.findall('n', s)
num = min(len(o), len(e), len(z), len(r))
len(n) - num
len(o) - num
len(e) - num
num2 = min(len(n), len(o), len(e))
for i in range(num2):
    print('1', end=' ')
for i in range(num):
    print('0', end=' ')
  
#ex12
import re
n = int(input())
s = input()
cnt = 0
while n > 0:
    x = re.findall('xxx', s)
    if len(x) > 0:
        cnt += 1
    s = s[1:]
    n -= 1
print(cnt)
