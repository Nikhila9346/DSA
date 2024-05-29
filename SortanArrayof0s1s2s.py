#DutchNationalFlagAlgorithm

#Sort an array with 0s, 1s and 2s

class DutchNationalFlag:
    def Sortanarray(self, n, arr):
        low = 0
        mid = 0
        high = n-1
        while mid <= high:
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        return arr

d = DutchNationalFlag()
print(d.Sortanarray(int(input("Enter the length of list:")),eval(input("Enter a list of 0s, 1s and 2s"))))


#output
# Enter the length of list:11
# Enter a list of 0s, 1s and 2s[0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0]
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2]

#gfg practice link - https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
#refer youtube video - https://youtu.be/tp8JIuCXBaU?si=YIcAHI7DkqZDUtLl

