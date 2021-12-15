#10. Demonstrate the use of append() function in 1D and 2D array.

import numpy as np

array_1d=np.array([1,2,3,4,5])
x=np.append(array_1d,6)
print("1D array",array_1d)
print("the use of append() function in 1D array",x)

array_2d=np.array([[1,2,3],[4,5,6]])
y=np.append(array_2d,np.array([[7,8,9]]),axis=0)
print("\n2D array")
print(array_2d)
print("the use of append() function in 2D array")
print(y)
