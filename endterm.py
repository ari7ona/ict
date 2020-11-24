#ex1
n = int(input())
index = 1
count = 0
while index < n:
  if n % index == 0:
    count += 1
  index += 1
print(count)

#ex2
def table(n, x):
    ans = 0
    for i in range(1, n + 1):
        if (x % i == 0 and x / i <= n):
            ans += 1
    return ans
n = int(input())
x = int(input())
print(table(n, x))

#ex3
n = input()
n = set(n)
if len(n) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
    
#ex4
y = int(input())
for i in range(y + 1, 9013):
    a = len(list(str(i)))
    b = len(set(list(str(i))))
    if a == b:
        print(i)
        break
    else:
        continue
      
#ex5
n = int(input())
aa = bb = cc = 0
for i in range(n):
    a, b, c = map(int, input().split())
    aa += a
    bb += b
    cc += c
if aa == bb == cc == 0:
    print("YES")
else:
    print("NO")
