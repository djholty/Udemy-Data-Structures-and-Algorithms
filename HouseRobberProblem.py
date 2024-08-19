#Problem: Given N houses along a street with some amount of money
# adjacent houses can't be stolen
# find the maximum amount that can be stolen
# [6,7,1,30,8,2,4]

def findMaxStealings(houselist, currenthouse=0):
    if currenthouse >= len(houselist):
        return 0
    else:    
        stealfirsthouse = houselist[currenthouse] + findMaxStealings(houselist, currenthouse+2) 
        stealsecondhouse = findMaxStealings(houselist, currenthouse +1)
    return max(stealfirsthouse, stealsecondhouse)

houses = [6,7,1,30,8,2,4]

print(findMaxStealings(houses,0))