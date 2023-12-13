import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
print("Array 1: ",arr1)
arr2 = np.array([6, 7, 8, 9, 10])
print("Array 2: ",arr2)

# Add arr1 and arr2 to create a new array called result_add.
result_add = arr1 + arr2
print("Sum: ",result_add)

#Multiply arr1 and arr2 to create a new array called result_multiply.
result_multiply = arr1 * arr2
print("Multiplication: ",result_multiply)

#Calculate the mean of result_add.
mean_result = np.mean(result_add)
print("Mean of Sum: ",mean_result)

#Find the maximum value in result_multiply.
max_value = np.max(result_multiply)
print("Maximum value of Multiplication: ",max_value)
