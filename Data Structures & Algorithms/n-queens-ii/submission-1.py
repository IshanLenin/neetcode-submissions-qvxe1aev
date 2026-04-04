class Solution:
    def totalNQueens(self, n: int) -> int:
        col=set()
        PosDiag=set()
        NegDiag=set()

        res=0
        def backtrack(r):
            nonlocal res
            if r == n:
                res +=1
                return

            for c in range(n):
                if c in col or (r+c) in PosDiag or (r-c) in NegDiag:
                    continue
            
                col.add(c)
                PosDiag.add(r+c)
                NegDiag.add(r-c)
                backtrack(r+1)
                col.remove(c)
                PosDiag.remove(r+c)
                NegDiag.remove(r-c)

        backtrack(0)
        return res