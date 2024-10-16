 #Given an array of intervals, find two numbers in the array that sum up to the target

class Solution:
  def twoSum(self, nums: List[int], target: int)
    h = {}
    for i, num in enumerate(nums):
      h[num] = i
    for i, num in enumerate(nums):
      desired = target - i
      if desired in h and h[desired] != i:
        return i, h[desired]
    
