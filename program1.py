def linear_search(arr, target):

    for index in range(len(arr)):
        if arr[index] == target:
            return index 
    return -1 

numbers = [5, 3, 8, 4, 2]
target_value = 4
result = linear_search(numbers, target_value)
print("Element found at index:",result)
