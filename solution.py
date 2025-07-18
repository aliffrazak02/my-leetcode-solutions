from typing import List
class Solution:

# 448. Find All Numbers Disappeared in an Array
# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.

# Brute Force Approach, O(n^2) time complexity, O(1) space complexity
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(1,len(nums)+1):
            if i not in nums:
                arr.append(i)
        return arr
    
# Hashset Approach, O(n) time complexity, O(n) space complexity
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        n = set(nums)
        arr = []
        for i in range(1,nums_length+1):
            if i not in n:
                arr.append(i)
        return arr

# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such
# that they add up to target. You may assume that each input would have exactly one solution
# and you may not use the same element twice. You can return the answer in any order


# Brute Force Approach, O(n^2) time complexity, O(1) space complexity    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            for j in range(0,len(nums)-1):
                for i in range(j+1,len(nums)):
                    if nums[j] + nums[i] == target:
                        return [j,i]
                    
                    
# Hash Map Approach, O(n) time complexity, O(n) space complexity
# O(n) for loop, O(1) for hash table lookup
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # x + y = target, target - x = y
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return [] # no solution found
    
    
# Optimized Hash Map Approach, O(n) time complexity, O(n) space complexity
# Instead of two loops, we can do it in one pass
# O(n) for loop, O(1) for hash table lookup    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # x + y = target, target - x = y
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement],i]
            numMap[nums[i]] = i
            
        return []

# 1365. How Many Numbers Are Smaller Than the Current Number
# Given the array nums, for each nums[i], find out how many numbers in the array are smaller than it. 
# That is, for each nums[i], you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

# Brute force solution
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] != nums[j] and nums[i]>nums[j]:
                    arr[i] += 1
        return arr

# 1266. Minimum Time Visiting All Points
# On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. 
# Return the minimum time in seconds to visit all the points in the order given by points.
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        res = 0
        for i in range(len(points)-1):
            res += max(
                abs(points[i+1][1]-points[i][1]),
                abs(points[i+1][0]-points[i][0])
                )
        return res

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        res = 0
        x1,y1 = points.pop()
        while points:
            x2, y2 = points.pop()
            res += max(abs(y2-y1),abs(x2-x1))
            x1, y1 = x2, y2

        return res

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        res = 0
        for i in range(len(points)-1):
            currX, currY = points[i]
            endX, endY = points[i+1]
            res += max(abs(endY-currY),abs(endX-currX))
        return res











