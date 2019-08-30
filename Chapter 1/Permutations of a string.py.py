class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = {}
        keys = counter.keys()
        for i in s1:
            if i in keys:
                counter[i] += 1
            else:
                counter[i] = 1
        odd = 0
        for i in counter:
            if counter[i] % 2 == 1:
                odd += 1
            if odd > 1:
                return False
        return True
                
