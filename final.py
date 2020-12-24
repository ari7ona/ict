#ex1
n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=0
for i in range(1,n):
    ans+=a[i]-a[i-1]-1
print(ans)

#ex2
t = int(input())
for i in range(t):
    n, m = list(map(int,input().split()))
    if n % m == 0:
        print('YES')
    else:
        print('NO')
           
#ex4
n = int(input())
s = input()
a = 0
b = 0
for i in range(n - 1):
	a += (s[i] + s[i + 1] == "SF")
	b += (s[i] + s[i + 1] == "FS")
print("YES" if a > b else "NO")
        
#ex5
def stair(value):
    ans = 1
    n = int(input())
    a = list(map(int, input().split()))
    a.append(1)
    vec = []
    for i in range(1, n + 1):
        if a[i] == 1:
            vec.append(a[i - 1])
    print(len(vec))
    print(*vec)
t = 1
for i in range(t):
    stair(i + 1)
