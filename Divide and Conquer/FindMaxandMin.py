def findMaxandMin(arr, left, right):
    if left == right:
        min, max = arr[left], arr[right]
        return min, max
    elif left == right-1:
        if arr[left] < arr[right]:
            min, max = arr[left], arr[right]
        else:
            min, max = arr[right], arr[left]
        return min, max
    else:
        mid = left + (right-left)//2
        min1, max1 = findMaxandMin(arr, left, mid)
        min2, max2 = findMaxandMin(arr, mid+1, right)
        min, max = compare(min1, min2, max1, max2)
        return min, max


def compare(min1, min2, max1, max2):
    if min1 < min2:
        min = min1
    else:
        min = min2
    if max1 < max2:
        max = max2
    else:
        max = max1
    return min, max


## Driver Code
arr = [75, 95, 45, 50, 65, 29, 32, 80]
left, right = 0, len(arr)-1
min_val, max_val = findMaxandMin(arr, left, right)
print(f"Maximum value: {max_val} | Minimum value: {min_val}") 