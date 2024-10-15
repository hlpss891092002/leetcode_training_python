# class Solution:
def search(nums: list[int], target: int) -> int:
        left = 0
        right =  len(nums) -1         
        while right >= left :
            med = int((left + right)/2)
            if nums[med] == target:
                return med
            if  nums[med] > target:
                right = med - 1  
            if  nums[med] < target:
                left = med + 1
        return -1

  