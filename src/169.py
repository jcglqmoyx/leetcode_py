class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = count = 0
        for num in nums:
            if num == res:
                count += 1
            else:
                count -= 1
            if count < 0:
                count = 1
                res = num
        return res
