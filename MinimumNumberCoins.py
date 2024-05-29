#GFG practice link -- https://www.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1

#Youtube link -- https://www.youtube.com/watch?v=mVg9CfJvayM

def MinimumNumberCoins(N):
    l = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    new_list = []

    for i in range(len(l)):
        while l[i] <= N:
            N -= l[i]
            new_list.append(l[i])
    return new_list

ans = MinimumNumberCoins(43)
print(ans)