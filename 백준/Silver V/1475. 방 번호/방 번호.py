import sys

n = sys.stdin.readline().strip()

# nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nums = list(0 for i in range(10))

for i in n:
    nums[int(i)] += 1
    if i == '6' and nums[6] > nums[9]:
        nums[6] -= 1
        nums[9] += 1
    elif i == '9' and nums[6] < nums[9]:
        nums[9] -= 1
        nums[6] += 1

print(max(nums))
