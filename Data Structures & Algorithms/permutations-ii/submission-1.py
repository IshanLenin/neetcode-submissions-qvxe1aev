class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count={n:0 for n in nums}
        res=[]
        perm=[]
        for n in nums:
            count[n]+=1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in count:
                if count[n]:
                    perm.append(n)
                    count[n]-=1
                    dfs()
                    count[n]+=1
                    perm.pop()
        dfs()
        return res