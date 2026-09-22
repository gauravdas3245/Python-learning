# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once. The
# relative order of the elements should be kept the same.

def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    k = 1 
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1
    return k
print("removing duplicates from sorted list")

nums1 = [1, 1, 2]
k1 = remove_duplicates(nums1)
print("Input:", [1, 1, 2])
print("k =", k1)
print("nums =", nums1[:k1])

# Check if an Array is Sorted
# Given an array, check whether the elements are arranged in ascending order.

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

print(" Checking if an Array is Sorted")
arr1 = [1, 2, 3, 7, 5]
print("Input:", arr1)
if is_sorted(arr1):
    print("Output: Yes")
else:
    print("Output: No")