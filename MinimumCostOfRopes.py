#final solution GFG link: https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1

#ABOUT HEAP DATASTRUCTURE: https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

import heapq

class Problem2:
    def MinimumCostOfRopes(self, arr, n):
        # creates a heap datastructure using arr
        heapq.heapify(arr)
        cost = 0

        for i in range(n-1):

            #heapq.heappop(arr) will remove the minimum element from the list, return that removed element and the order is adjusted
            add = heapq.heappop(arr) + heapq.heappop(arr)
            cost += add

            #heapq.heappush(arr) will add the given element to the heap and order is adjusted
            heapq.heappush(arr, add)

        return cost

n = int(input("Enter the no.of elements:"))
arr = eval(input("Enter the list"))
p2 = Problem2()
print(p2.MinimumCostOfRopes(arr, n))

#OUTPUT
# Enter the no.of elements:5
# Enter the list[4, 2,7, 6,9]
# 62

#################################################################################################################

# #solved by me
#
# l = [4, 2, 7, 6, 9]
# # l = [4, 3, 2, 6]
# cost = 0
# n = len(l)
# # print(n)
#
# for i in range(n-1):
#     l2 = sorted(l)
#     # print(l2)
#     # print(f"the cost before {cost}")
#     app =l2[0] + l2[1]
#     cost += app
#
#     # print(f"the cost after {cost}")
#     if len(l2) >= 2:
#         for i in range(2):
#             l2.pop(0)
#     l2.append(app)
#     # print(l2)
#     l = l2
# print(cost)

########################################################################################################

#by using heap

# import heapq
#
# l =[4, 2, 7, 6, 9]
# cost = 0
# n = len(l)
#
# heapq.heapify(l)
# # print(l)
#
# for i in range(n-1):
#     add = heapq.heappop(l) + heapq.heappop(l)
#     cost += add
#
#     heapq.heappush(l, add)
# print(cost)

#############################################################################




