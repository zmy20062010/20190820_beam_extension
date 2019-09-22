import numpy as np

x = np.ones((3))
print(np.transpose(x).shape, x.shape)



my_array = np.array([1,2,3])

my_array_T = np.transpose(np.matrix(my_array))

print(my_array, my_array_T, my_array.reshape(-1, 1), my_array.reshape(1, -1))