import  numpy as np
from numpy.ma.core import dot

arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]])
print(arr.mean())
print(arr.sum())
print(arr.max())
print(arr.min())
matrix1 = np.array([[6, 7],
                    [11, 5]])
matrix2 = np.array([[11, 10],
                    [10, 5]])
print(matrix1+matrix2)
print(matrix1*matrix2)
print(np,dot(matrix1,matrix2))