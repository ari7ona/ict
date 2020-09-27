#ex1
w1 = int(input("Enter the vertical position of white rook: "))
w2 = int(input("Enter the horizontal position of white rook: "))
b1 = int(input("Enter the vertical position of black rook: "))
b2 = int(input("Enter the horizontal position of black rook: "))
if (w1 - b1)*(w2 - b2) == 0:
    print("YES")
else:
    print("NO")
#ex2
c = int(input())
r = int(input())
nc = int(input())
nr = int(input())
if (c == nc + 1 or c == nc - 1 or c == nc) and (r == nr + 1 or r == nr - 1 or r == nr):
    print("YES")
else:
    print("NO")
#ex3
c = int(input())
r = int(input())
nc = int(input())
nr = int(input())
if c == r and nc == nr:
    print("YES")
else:
    print("NO")
#ex4
c = int(input())
r = int(input())
nc = int(input())
nr = int(input())
if c == nc or r == nr or abs(c - nc) == abs(r - nr):
    print("YES")
else:
    print("NO")
#ex5
c = int(input())
r = int(input())
nc = int(input())
nr = int(input())
if nc - c == 1 and nr - r == 2:
    print("YES")
else:
    print("NO")
#ex6
n = int(input())
m = int(input())
k = int(input())
if (n * m) < k:
    print("NO")
elif (k % m) == 0 or (k % n) == 0:
    print("YES")
else:
    print("NO")
#ex7
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if c < d:
    print(c)
else:
    print(d)
#ex8
a = []
for i in range(3):
    inp = int(input())
    a.append(inp)
a.sort()
for i in range(3):
    print(a[i], end = ' ')
#ex9
a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
volume1 = a1 * b1 * c1
volume2 = a2 * b2 * c2
if (volume1 == volume2):
    print("Boxes are equal")
elif (volume1 < volume2 or volume1 > volume2 ):
    print("Possible")
#ex10
n = int(input())
for i in range(1, n):
    if (i**2 <= n):
        print(i**2)
#ex11
n = int(input())
for i in range(2, n):
    if (n % i == 0):
        print(i)
        break
#ex12
n = int(input())
arr = []
for i in range(0, n):
    if (2**i < n):
        print(2**i)
#ex13
a = []
sum = 0;
while True:
    inp = int(input())
    a.append(inp)
    if inp == 0:
        break
for i in range(0, len(a)):
    sum = sum + a[i];
print(sum)
#ex14
a = []
max = 0
cnt = 0
while True:
    inp = int(input())
    a.append(inp)
    if inp == 0:
        break
for i in range(0, len(a)):
    if(a[i] > max):
        max = a[i]
for i in range(0, len(a)):
    if(a[i] == max):
        cnt = cnt + 1
print(cnt)
#ex15
a = int(input())
index = int
arr = [1, 2]
for i in range(2,700):
    arr.append(arr[i-1]+arr[i-2])
index = arr.index(a)
print(index + 2)
#ex16
a = []
lm = 0
while True:
    inp = int(input())
    a.append(inp)
    if inp == 0:
        break
for i in range(len(a)):
    if a[i - 1] < a[i] > a[i + 1]:
        lm = a[i]
print(lm)
#ex17
def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num
n = int(input())
List = []
for i in range(n):
    inp = int(input())
    List.append(inp)
print(most_frequent(List))
#ex18
a = int(input())
arr = []
for i in range(a):
    inp = int(input())
    arr.append(inp)
last = arr[len(arr) - 1]
for i in range(a):
    temp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = temp
arr[0] = last
print(arr)
#ex19
x = int(input())
arr = []
cnt = 0
for i in range(x):
    inp = int(input())
    arr.append(inp)
arr.sort()
i = 0
while i < (x - 1):
    if arr[i] == arr[i + 1]:
        cnt += 1
        i = i + 2
    else:
        i += 1
print(cnt)
