from math import *

n = int(input("Enter any number:"))
trailing_zeros = 0
power_of_five = 5

while n >= power_of_five:
    trailing_zeros += floor(n/power_of_five)
    # print(floor(n/power_of_five))
    power_of_five = power_of_five * 5

print(trailing_zeros)

######################################################################

# import math
#
# n = 25
# trailing_zeros = 0
# calculated_zero = 1
# i = 1
#
# while calculated_zero > 0:
#     calculated_zero = math.floor(n/5 ** i)
#     trailing_zeros += calculated_zero
#     i +=1
# print(trailing_zeros)
