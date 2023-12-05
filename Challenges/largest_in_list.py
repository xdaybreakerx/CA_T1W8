def find_largest_num(nums):
    largest_num = 0
    for i in nums:
        largest_num = max(largest_num, i)
    return largest_num