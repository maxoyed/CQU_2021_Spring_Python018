def get_degree(arr):
    items = list(set(arr))
    counts = [arr.count(item) for item in items]
    counts.sort(reverse=True)
    return counts[0]


nums = eval(input())
nums_degree = get_degree(nums)
min_length = len(nums)

for i in range(len(nums)+1):
    for j in range(1, len(nums)+1 - i):
        if get_degree(nums[i:i+j]) == nums_degree and len(nums[i:i+j]) < min_length:
            min_length = len(nums[i:i+j])

print(min_length)
