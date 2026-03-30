class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preFix = [1]
        reversed_sufFix = [1]

        for i in range(1, len(nums)):
            preFix.append(nums[i - 1] * preFix[i - 1])
        
        reversed_nums = nums[::-1]

        for i in range(1, len(reversed_nums)):
            reversed_sufFix.append(reversed_nums[i - 1] * reversed_sufFix[i - 1])
        
        sufFix = reversed_sufFix[::-1]

        res = []

        for i in range(len(preFix)):
            res.append(preFix[i] * sufFix[i])
        
        return res