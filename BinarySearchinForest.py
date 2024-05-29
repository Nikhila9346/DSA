#GFG practice link --- https://www.geeksforgeeks.org/problems/binary-search-in-forest--141631/1
#youtube solution link -- https://youtu.be/2E73SftV0co?si=UNyS4qSn3JyYFW6I

#Can be referred as WOOD CUTTING PROBLEM

class Solution:
    def find_height(self, tree, n, k):
        # code here
        low = 0
        high = max(tree)

        while low <= high:
            mid = (low + high) // 2
            wc = 0
            #for every array element, subtract the calculated mid value to get the wood cut
            for height in tree:
                if height > mid:
                    wc += height - mid

            #if woodcut is equals to required woodcut then return the mid value(the height where the tree should be cut down)
            if wc == k:
                return mid
            #if the woodcut is greater than the required one then the woodcut height should be increased
            elif wc > k:
                low = mid + 1
            #if the woodcut is lesser than the required one then the woodcut height should be decreased
            else:
                high = mid - 1
        return -1


f = Solution()
print(f.find_height([1, 7, 6, 3, 4, 7], 6, 8))