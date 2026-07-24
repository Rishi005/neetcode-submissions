class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
        # for i, num in enumerate(nums[1:]):
        #     if nums[i] == num:
        #         return True
        # return False
            
        