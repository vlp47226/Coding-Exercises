
#From https://www.deep-ml.com/problems/1
#Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector
#Input: a = [[1,2],[2,4]], b = [1,2]
#Output: [5, 10]
def matrix_dot_vector(a, b):
	c = []
	if a and b: #Check if a and b are valid
		for a_m in a:
			if (len(a_m) == len(b)): #Make Sure that the length of the matrix row is equal to the length of the vector
				newVal = 0
				for a_n, b_n in  zip(a_m,b): #Iterate through the matrix row and the vector
					newVal += a_n*b_n #Calculate the dot product
				c.append(newVal) #Add the dot product to the result list
			else:
				return -1
	else:
		return -1
	return c

if "__main__" == __name__:
    a = [[1,2],[2,4]]
    b = [1,2]
    print("Matrix Dot Vector: For test case data: ", a, " and ", b)
    print("Output: ", matrix_dot_vector(a, b))
    print("Is matrix_dot_vector correct?: ", matrix_dot_vector(a, b) == [5, 10])