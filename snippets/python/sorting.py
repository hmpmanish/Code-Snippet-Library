def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
numbers = [64, 25, 12, 22, 11]
sorted_numbers = bubble_sort(numbers)
print("Sorted array:", sorted_numbers)
