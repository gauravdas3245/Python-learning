# ---------- Problem 2: Find Largest and Smallest Elements ----------



def find_max_min(arr):
    maximum = arr[0]
    minimum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
        if arr[i] < minimum:
            minimum = arr[i]
    return maximum, minimum


print(" Largest and Smallest Elements")
arr = [12, 5, 78, 34, 9, 56]
maximum, minimum = find_max_min(arr)
print("Input:", arr)
print("Maximum =", maximum)
print("Minimum =", minimum)