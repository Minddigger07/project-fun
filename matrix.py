

import numpy as np
mat1=np.arange(1,10).reshape(3,3)
mat2=np.arange(1,10).reshape(3,3)
print(f"Matrix 1:\n{mat1}")
print(f"Matrix 2:\n{mat2}")
print(f"Sum of 2 matrices:\n{np.add(mat1,mat2)}")
print(f"Difference of 2 matrices:\n{np.subtract(mat2,mat1)}")
print(f"Product of 2 matrices:\n{np.dot(mat1,mat2)}")
print(f"Transpose matrix 1:\n{np.transpose(mat1)}")

