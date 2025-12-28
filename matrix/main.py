import numpy as np

arr1 = np.array([
    [122, 151, 787],
    [686, 767, 222],
    [333, 444, 555]
])

# for i in range(len(arr1)): 
#     print(min(arr1[i]))
#     print(max(arr1[i]))


arr2 = np.array([
    [123, 456, 666],
    [222, 333, 451],
    [21, 323, 444]
])


def find_saddle_points(matrix):
    minimums = []
    maximumx = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            print(matrix[j][i])

find_saddle_points(arr1)