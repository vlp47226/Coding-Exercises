
#TwoSum
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    data = {}
    for i,num in enumerate(nums):
        diff = target - num
        if diff in data:
            return [data[diff], i]
        else:
            data[num] = i
    return []

if __name__ == '__main__':
    data = [2, 7, 11, 15]
    target = 18
    print("TwoSum: For test case data: ", data, " and target: ", target)
    print(twoSum(data, target))
    print("Is twoSum correct?: ", twoSum(data, target) == [1,2])

    