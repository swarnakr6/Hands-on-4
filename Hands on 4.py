#!/usr/bin/env python
# coding: utf-8

# Problem 0
# 
# Implementation of Fibonacci sequence

# In[2]:


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def debug_fib(n):
    def fib_debug(n, depth=0):
        print("  " * depth, "fib({})".format(n))
        if n == 0:
            print("  " * depth, "--> return 0")
            return 0
        if n == 1:
            print("  " * depth, "--> return 1")
            return 1
        print("  " * depth, "--> fib({}) + fib({})".format(n-1, n-2))
        return fib_debug(n-1, depth+1) + fib_debug(n-2, depth+1)

    result = fib_debug(n)
    print("Result:", result)
    return result

debug_fib(5)


# Problem 1
# 
# Given K sorted arrays of size N each, the task is to merge them all maintaining their sorted order.

# In[3]:


import heapq

def merge_sorted_arrays(arrays):
    merged = []
    heap = []

    # Initialize heap with the first element of each array
    for i, array in enumerate(arrays):
        if array:  # Make sure the array is not empty
            heapq.heappush(heap, (array[0], i, 0))

    while heap:
        val, arr_index, index = heapq.heappop(heap)
        merged.append(val)

        # Move to the next element in the array
        if index + 1 < len(arrays[arr_index]):
            next_val = arrays[arr_index][index + 1]
            heapq.heappush(heap, (next_val, arr_index, index + 1))

    return merged

# Example usage:
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]
array3 = [0, 9, 10, 11]

arrays = [array1, array2, array3]
merged_array = merge_sorted_arrays(arrays)
print(merged_array)


# 2.
# Time Complexity:
# Building the initial heap: It takes O(KN) time to go through each of the K arrays once in order to build the initial heap.
# merging elements: We pop one element from the heap (which takes O(logK) time) and push a new element from the same array onto the heap (which also requires O(logK) time) for each iteration. Until all the components are combined, this process keeps going. The entire time complexity of merging is O(KN * logK) due to the KN elements.
# As a result, the algorithm's total time complexity is O(KN * logK).
# 
# 3. 
# Ways to Improve the Implementation:
# Insertion with Binary Search: Rather than employing a list, we may utilise a binary search to determine the exact location of the subsequent element to be added to the combined array. This can lower the complexity of the insertion time from O(logK) to O(logN).
# Employ Priority Queues: We might use a priority queue data structure, which is designed for these kinds of operations, instead of the given solution, which uses a list as a heap.
# Merge operations in parallel: We could combine several arrays at once to increase performance if the arrays are big and the system allows parallelism.
# 
# 
# 
# ________________________________________________________________________________________________________________________________
# 
# 
# Problem 2
# 
# Given a sorted array array of size N, the task is to remove the duplicate elements from the array.

# In[4]:


def remove_duplicates(arr):
    if not arr:
        return []

    # Initialize variables
    n = len(arr)
    unique_index = 0

    # Traverse through the array
    for i in range(1, n):
        # If the current element is different from the previous one
        if arr[i] != arr[unique_index]:
            unique_index += 1
            # Move the unique element to the next position
            arr[unique_index] = arr[i]

    # Slice the array to keep only the unique elements
    return arr[:unique_index + 1]

# Example usage:
array1 = [2, 2, 2, 2, 2]
array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]

print("Original array 1:", array1)
result1 = remove_duplicates(array1)
print("Array with duplicates removed:", result1)

print("Original array 2:", array2)
result2 = remove_duplicates(array2)
print("Array with duplicates removed:", result2)


# 2.
# Time Complexity:
# Traversing the array: The algorithm requires O(N) time to traverse the array once.
# Eliminating duplicates: Every element in the traversal is compared to its predecessor, and if there is a difference, it is moved to the next location. It takes O(1) time per element because this procedure only occurs once.
# As a result, the algorithm's total time complexity is O(N).
# 
# 3.
# Ways to Improve the Implementation:
# Use Two Pointers: We may use the two pointers technique, where one pointer scans the array and the second pointer keeps track of the spot where the next unique element should be inserted, to move elements rather than one at a time.
# Set up Removal: In the given implementation, the unique elements are stored in a new array that is created. To get rid of duplicates, we may alter the array while it's still in use.
# If the array wasn't sorted, we could find duplicates more quickly by using a binary search, which also lowers the time complexity.

# In[ ]:




