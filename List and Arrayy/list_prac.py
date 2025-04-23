sample_list = [ 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10]
print(sample_list)

list1 = sample_list.copy()
list1[2] = 100

print(sample_list, list1)

lis2 = sample_list.copy()
lis2[2:6] = [100, 200, 300, 400]
print(sample_list, lis2)

compre = [x for x in sample_list if x % 2 == 0]
compre2 = [2 * x for x in sample_list if x % 2 == 0]
odd_even = ['odd' if x % 2 != 0 else 'even' for x in sample_list]
prime_composite = ['prime' if x % 2 != 0 else 'composite' for x in sample_list]


print(compre)
print(compre2)
print(odd_even)
print(prime_composite)

# slicing

print(sample_list[2:5])
print(sample_list[-5:-2])
print(sample_list[::1])


# 2d list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print([matrix[item] for item in range(len(matrix))])
print([[row[i] for row in matrix] for i in range(len(matrix[0]))])


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()


# average of something
grade = [77, 88, 90, 100, 44, 78, 88]
ave = sum(grade) // len(grade)
print(ave)

# lamda 

list_of_name = ['abc', 'def', 'ghi', 'jkl', 'mno']

x  = lambda x: x[0].upper()
z = map(x, list_of_name)
listed = map(lambda x: x.split(), list_of_name)
print(list(z))
print(list(listed))

seee = set([1, 2, 3, 4, 5, 6]) - set([1, 2, 3, 4, 6])
print(seee)
print()