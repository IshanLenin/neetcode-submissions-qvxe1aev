class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        from collections import Counter

        s1Count = Counter(s1)
        windowCount = Counter(s2[:len(s1)])

        if s1Count == windowCount:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            windowCount[s2[r]] += 1
            windowCount[s2[l]] -= 1
            if windowCount[s2[l]] == 0:
                del windowCount[s2[l]]
            l += 1
            if s1Count == windowCount:
                return True
        
        return False
