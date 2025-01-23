
#TwoSum
#Find the indices of the two numbers such that they add up to a specific target.
#Example Input: nums = [2, 7, 11, 15], target = 9
#Example Output: [0, 1]
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    data = {} #Init Dictionary to store the data
    for i,num in enumerate(nums):
        diff = target - num #Calculate the different between the target and the current number
        if diff in data: #If the difference is in the dictionary, return the index of the difference and the current index
            return [data[diff], i] #This works because a + b = y and y - a = b and y - b = a are the same
        else:
            data[num] = i #If the difference is not in the dictionary, add the current number to the dictionary
    return [] #If no solution is found, return an empty list

# if __name__ == '__main__':
#     data = [2, 7, 11, 15]
#     target = 18
#     print("TwoSum: For test case data: ", data, " and target: ", target)
#     print(twoSum(data, target))
#     print("Is twoSum correct?: ", twoSum(data, target) == [1,2])

#Ocean View
#Given an array of building heights, return the number of buildings that have an ocean view.
#The Ocean is on the right side of the array.
#Example Input: [3, 7, 8, 3, 6, 1]
#Example Output: 3

def findBuildings(heights: list[int]) -> list[int]:
    max = 0 
    result = [] #Init result list
    for i in range(len(heights) -1, -1, -1): #Traverse the list of heights backwards (right to left)
        height = heights[i] #get the height of the current building
        if max < height: #If the height of the current building is greater than the max height, add the index to the result list
            result.append(i)
            max = height
    return result[::-1]   #Return the result list in reverse order since we traversed the list backwards

# if __name__ == '__main__':
#     data = [3, 7, 8, 3, 6, 1]
#     print("Ocean View: For test case data: ", data)
#     print("Output: ", findBuildings(heights=data))
#     print("Is findBuildings correct?: ", len(findBuildings(heights=data)) == 3 and findBuildings(heights=data) == [2, 4, 5])