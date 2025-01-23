#From https://www.deep-ml.com/problems/97
#Implement the ELU (Exponential Linear Unit) activation function, which helps mitigate the limitations of ReLU by providing negative outputs for negative inputs.
#The function should compute the ELU activation value for a given input.
#Input: elu(-1)
#Output: -0.6321

import math
def elu(x, alpha=1.0):
    """
	Compute the ELU activation function.

	Args:
		x (float): Input value
		alpha (float): ELU parameter for negative values (default: 1.0)

	Returns:
		float: ELU activation value
	"""

    if x > 0:
        val = x
    else:
        val = alpha*(math.exp(x)-1)
    
    return float(round(val,4))

if "__main__" == __name__:
    x = -1
    alpha = 1.0
    print("ELU activation: For test case data: ", x, " and ", alpha)
    print("Output: ", elu(x, alpha))
    print("Is matrix_dot_vector correct?: ", elu(x, alpha) == -0.6321)