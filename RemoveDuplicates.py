

def removeDuplicates(nums):
    # length = len(nums)
    #
    # i, j = 0, 1
    # while j < length:
    #     if nums[j] != nums[i]:
    #         i += 1
    #         nums[i] = nums[j]
    #     j += 1
    #
    # return i + 1

    i = 0
    for num in nums:
        if nums[i] != num:
            i += 1
            nums[i] = num
    # a = len(nums) and i + 1
    return len(nums) and i + 1

'''
要判断A and B 是真是假，首先python会先判断A，如果A是真的，那就判断B，不管B是真是假，python都会return B，
因为如果B是真的，那A and B就是真的，B是假的，那A and B就是假的.
（另外说明，在python中0是false，其他数字均默认为true，所以2 and 3,先判断了2是真的，那么python就接着看下一个3，
不管3是真是假，返回3总是不会错的。同理，3 and 2 就是返回2了 ）
'''

# nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2,2,2,2,2]

# print(removeDuplicates(nums))

nn = removeDuplicates(nums)
for i in range(nn):
    print(nums[i])