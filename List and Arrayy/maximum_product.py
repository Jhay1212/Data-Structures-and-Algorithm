from types import List
def max_product(list: List[int]) -> int:
    """
    :type list: List[int]
    :rtype: int
    Big O(n)
    Find the maximum product in an array
    """
    return sorted(list)[-1] * sorted(list)[-2]