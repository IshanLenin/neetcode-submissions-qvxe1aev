class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        window=set()

        for R in range(len(nums)):
            if R-L>k:
                window.remove(nums[L])
                L +=1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
        