# Write a program to find all pairs of integers whose sum is
# equal to a given number:
#question initially asks for pairs of numbers, but course gave
#pairs of indices

# Qs to ask:
# Does array contain positive and negative numbers?
# What if same pair occurs twice, should it be printed twice
# Should the reverse be printed as well?
# Should each pair have distinct integers only?
# How big is array?

#my solution
def findpairs(array, targetnum):
    pairset = set()
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetnum:
                pairset.add((array[i], array[j]))
    return pairset

myarray = [1,2,3,4,5,1,2,6,7]

print(list(findpairs(myarray, 5)))

#course solution
    # def two_sum(nums, target):
    #     seen = {}
        
    #     for i, num in enumerate(nums):
    #         complement = target - num
            
    #         if complement in seen:
    #             return [seen[complement], i]
            
    #         seen[num] = i
     
    # nums = [2, 7, 11, 15]
    # target = 9
    # indices = two_sum(nums, target)
    # print(f"Indices of the two numbers are: {indices}")