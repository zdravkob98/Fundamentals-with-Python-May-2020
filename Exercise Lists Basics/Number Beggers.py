num_str = input().split(',')
#print(f'num_str {num_str}')

count = int(input())

result = [0] * count

nums = []

for num in num_str:
    nums.append(int(num))
#print(f'nums {nums}')

for i in range(len(nums)):
    index = i % count
    result[index] += nums[i]
print(result)