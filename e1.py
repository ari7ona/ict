n = int(input())
index = 1
count = 0
while index < n:
  if n % index == 0:
    count += 1
  index += 1
print(count)