def longestConsecutive(nums):
    nums = set(nums)
    table = {}
    maxval = 0
    for num in nums:
        x = table.get(num - 1, 0)
        y = table.get(num + 1, 0)
        val = x + y + 1
        table[num - x] = val
        table[num + y] = val
        maxval = max(maxval, val)
        print("num", num, "x", x, "y", y, "val", val, "max", maxval)
        print("table", table)
    return maxval
result = longestConsecutive([0,3,7,2,5,8,4,6,0,1])
print(result)