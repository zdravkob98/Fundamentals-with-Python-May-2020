text = input().split()
n = int(input())

nums =[]
for num in text:
    nums.append(int(num))
result = [] + nums
l = []

for i in range(n):
    nums.sort()
    l.append(nums.pop(0))
for i in range(n):
    if l[i]  in result:
        result.remove(l[i])
print(result)
