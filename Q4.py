import numpy as np
from scipy.linalg import svd

matrix_A = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
print("MATRIX A: ")
print(matrix_A)

matrix_B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("MATRIX B: ")
print(matrix_B)

# Add matrix_A and matrix_B element-wise to create a new matrix, matrix_sum.
matrix_sum = matrix_A + matrix_B
print("MATRIX SUM: ")
print(matrix_sum)

# Multiply matrix_A and matrix_B element-wise to create a new matrix, matrix_product.
matrix_multiply = matrix_A * matrix_B
print("MATRIX MULTIPLY: ")
print(matrix_multiply)

# Calculate the matrix product of matrix_A and matrix_B (dot product) and  store it in matrix_dot.
matrix_dot = np.dot(matrix_A, matrix_B)
print("MATRIX dot MULTIPLY: ")
print(matrix_dot)

# Transpose matrix_A and store it in matrix_A_transpose.
matrix_A_transpose=np.transpose(matrix_A)
print("MATRIX A Transpose: ")
print(matrix_A_transpose)

# Calculate the determinant of matrix_B and store it in determinant_B.
determinant_B=np.linalg.det(matrix_B)
print("MATRIX B Determinant: ",determinant_B)

# Find the eigenvalues and eigenvectors of matrix_A and store them in eigenvalues_A and eigenvectors_A.
eigenvalues_A , eigenvectors_A = np.linalg.eig(matrix_A)

# printing eigen values
print("The Eigen values of Matrix A :\n",eigenvalues_A)

# printing eigen vectors
print("Printing eigenvectors of Matrix A :\n",eigenvectors_A)

# SVD
U, s, VT = svd(matrix_A)
print(U)
print(s)
print(VT)
