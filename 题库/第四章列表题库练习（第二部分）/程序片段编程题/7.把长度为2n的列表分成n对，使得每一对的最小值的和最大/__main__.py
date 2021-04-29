def maxsum(nums):
    nums.sort()
    unzip = list(zip(*[iter(nums)]*2))
    return sum(list(map(lambda item: item[0], unzip)))


nums = eval(input())
v = maxsum(nums)  # 调用自定义函数
print(v)
