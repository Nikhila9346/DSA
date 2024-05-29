# KADANES ALGORITHM
#
# set sum = 0
# set maximum = any element in the given array [let's say arr[0]]
#
# It will helps us to iterate throught the given array.
# While traversing, you need to add every element of that array to sum
#
# During iteration, if you find
# - the sum is getting to the negative values
#   then set the sum = 0
# - if the calculated sum is greater than the maximum
#   then set maximum = sum

#USING KADANES ALGORITHM

arr = [1, 2, 3, -2, 5]
# arr = [-1, -2, -3, -4]
n = len(arr)

sort = sorted(arr)
maximum = sort[0]

sum = 0
for i in range(n):
    sum += arr[i]
    if sum > maximum:
        maximum = sum
    if sum < 0:
        sum = 0

print(maximum)

############################################################################################################

#Max Subarray Sum
import array

# arr = [1, 2, 3, -2, 5]
# # arr = [-1, -2, -3, -4]
# n = len(arr)
#
#
# sort = sorted(arr)
# maximum = sort[n-1]

# for i in range(n):
#     for j in range(i, n):
#         sum1 = 0
#         for j in range(j+1):
#             sum1 += arr[j]
#         if sum1 > maximum:
#             maximum = sum1

# print(maximum)

#optimizing this part

# for i in range(n):
#     sum1 = 0
#     for j in range(i, n):
#         sum1 += arr[j]
#         if sum1 > maximum:
#             maximum = sum1
#
# print(maximum)

###########################################################################################





