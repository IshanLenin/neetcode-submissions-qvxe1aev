class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R,D = deque(), deque()

        for i,c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)

        while R and D:
            RVal = R.popleft()
            DVal = D.popleft()

            if RVal < DVal:
                R.append(RVal + len(senate))
            else:
                D.append(DVal + len(senate))
        
        return "Radiant" if R else "Dire"
        