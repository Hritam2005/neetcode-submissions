class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check={}
        for i,j in enumerate(nums):
            diff=target-j

            if diff in check:
                return[check[diff],i]
            check[j]=i