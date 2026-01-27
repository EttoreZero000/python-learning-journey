from clases import *

def two():
    string = input("Enter the name fuction: ")
    print(string.replace(" ", "_").lower())

def two_sum():
    nums = [2,7,11,15]
    target = 9

    if not (len(nums) >= 2 and len(nums) <= 10**4):
        raise ValueError("The size is incorrect")
    
    for num in nums:
        if not(-10**9 <= num and 10**9 >= num):
            raise ValueError("The numbers is very big or very less")
        
    if not(-10**9 <= target and target <= 10**9):
        raise ValueError("The target is very big or very less")
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j] == target and not(i==j):
                return [i,j]
class Solution:            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: