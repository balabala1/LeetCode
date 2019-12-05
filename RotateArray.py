

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n
    nums[:] = nums[n - k:] + nums[:n - k]

# nums = [1,2,3,4,5,6,7]
# k = 3
# rotate(nums, k)
# print(nums)