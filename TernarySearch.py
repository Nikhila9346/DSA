arr = [7, 12, 19, 24, 31, 48, 51, 63, 67, 73, 81, 92]

r = len(arr)
l = 0

key = 19 #element to be searched
pos = -1
# print(l,r)
while l <= r:

    mid1 = l + (r - l) // 3
    mid2 = r - (r - l) // 3

    if key == arr[mid1]:
        pos = mid1
        break
    elif key == arr[mid2]:
        pos = mid2
        break
    elif key < arr[mid1]:
        r = mid1 - 1
    elif key > arr[mid2]:
        l = mid2 + 1
    else:
        l = mid1 + 1
        r = mid2 - 1


print(pos)