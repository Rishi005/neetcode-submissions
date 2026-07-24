class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {nums[0]: [0]}
        for i, num in enumerate(nums[1:]):
            diff = target - num
            if diff in diffs:
                return [diffs[diff][0], i+1]
            if num not in diffs:
                diffs[num] = []
            diffs[num].append(i+1)

