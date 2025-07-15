# Learning about the various searching algorithms 

# Linear Search --> Time Complexity: 0(n) ------ Traverse through each element

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
        else:
            return False
        
# Binary Search --> Time Complexity: 0(logn) ----- Divide and conquer strategy

def binary_search(data, target):
    lowIndex = 0
    highIndex = len(data) - 1


    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

# Challenge: Integer Square Root
# Objective is to find the largest integer whose square is <= the given integer

def integer_square_root(x):
    low = 0
    high = x

    while low <= high:
        mid = (low + high) // 2
        midSqred2 = mid * mid

        if midSqred2 <= x:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1


x = 400
print(integer_square_root(x))


# Challenge: Cyclically Shifting an Array

def find(X):

    low = 0
    high = len(X) - 1

    while low < high:
        mid = (low + high) // 2

        if X[mid] > X[high]:
            low = mid + 1
        elif X[mid] <= X[high]:
            high = mid

    return low

X = [4, 35, 6, 7, 1001, 2111, 3]

newArr = find(X)

print(X[newArr])