import numpy as np

# Create array
arr = np.array([
                    [
                        [1, 2, 3],
                        [2, 4, 3],
                        [7, 2, 1]
                    ],
                    [
                        [1, 2 , 4],
                        [2, 4, 3],
                        [7, 2, 1]
                    ]
                ]) 
print(arr)
print(arr.shape)

# Reshape 
# arr = arr.reshape(1, 3)
# print(arr)  
# print (arr.shape)

# flatten_array = arr.flatten()
# print(flatten_array)
# print(flatten_array.shape)

# # Stack vertically  
# arr1 = np.array([1, 2])

arr2 = np.array([
                    [
                        [1, 2, 3],
                        [2, 4, 3],
                        [7, 2, 1]
                    ],
                    [
                        [1, 2 , 4],
                        [2, 4, 3],
                        [7, 2, 1]
                    ]
                ]) 

# arr2 = np.array([3, 4])
stacked = np.vstack([arr, arr2])
# print(stacked)
# print(stacked.shape)

sliced = arr[0:1]
print(sliced)
print(sliced.shape)