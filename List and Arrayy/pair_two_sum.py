def pair_of_two_sums(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: Lis[int]
    Big O(n^2)
    """
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                res.append([i, j])
    return 'not found' if not res else res
            


def pair_of_two_sums2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    Big O(n)
    """
    nums_map = {}
    for i in range(len(nums)):
        nums_map[nums[i]] = i
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums_map and nums_map[diff] != i:
            return [i, nums_map[diff]]
    return 'not found'
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    nums2 = [ i for i in range(100)]
    num3 = [99, 122, 123 ]
    print(pair_of_two_sums(nums, 9))
    print(pair_of_two_sums(nums2,66))
    print(pair_of_two_sums(num3, 9))
    print(pair_of_two_sums2(nums, 9))
    print(pair_of_two_sums2(nums2, 66))
    print(pair_of_two_sums2(num3, 9))
    