def twosum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums = sorted(nums)
    left, right = 0, len(nums) - 1
    maxv = -1
    while not left == right:
        total = nums[left] + nums[right]
        if total >= k:
            right = right - 1
        else:
            maxv = max(maxv, total)
            left = left + 1
    return maxv
print(twosum([34,23,1,24,75,33,54,8], 60))