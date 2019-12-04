
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # length = len(nums)
    # i, j = 0, 1
    # while j < length:
    #     if nums[j] != nums[i]:
    #         i += 1
    #         nums[i] = nums[j]
    #     j += 1
    # return i + 1

    # 改进版
    i = 0
    for num in nums:
        if num != nums[i]:
            i += 1
            nums[i] = num
    return len(nums) and i + 1  # 若len(nums)为真，那么总是返回i+1

'''
要判断A and B 是真是假，首先会判断A，如果A是假，则返回A；如果A是真的，那就判断B，不管B是真是假，python都会return B，
因为如果B是真的，那A and B就是真的，B是假的，那A and B就是假的.
（另外说明，在python中0是false，其他数字均默认为true。同理，3 and 2 就是返回2了 ）
'''


# nums = [0,0,1,1,1,2,2,3,3,4]
#
# n_len = removeDuplicates(nums)
# for i in range(n_len):
#     print(nums[i])