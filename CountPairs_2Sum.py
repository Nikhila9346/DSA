#gfg practice link -- https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1


def getPairsCount(arr, n, k):
    # code here
    hash_map = {}
    count = 0
    for t in arr:
        diff = k - t
        # print(diff)
        if diff in hash_map:
            # print(hash_map)
            count += hash_map[diff]
            # print(count)
        if t in hash_map:
            hash_map[t] += 1
        else:
            hash_map[t] = 1
        # print(hash_map)
    return count

# print(getPairsCount([1,5,7,1], 4, 6))
print(getPairsCount([1,5,5,5,5,7], 4, 10))