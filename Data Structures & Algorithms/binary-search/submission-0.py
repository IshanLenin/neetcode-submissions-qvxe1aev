class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)

        while l<r:
            m=l+((r-l)//2)
            if nums[m] >= target:
                r=m
            elif nums[m] < target:
                l=m+1
        return l if (l<len(nums) and nums[l]==target) else -1
        