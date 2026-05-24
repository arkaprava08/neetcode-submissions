class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charMap = defaultdict(int)

        for c in s:
            charMap[c]+=1
        
        for c in t:
            if c in charMap:
                charMap[c]-=1
                if charMap[c] == 0:
                    charMap.pop(c)
            else:
                return False
        
        if charMap.items():
            return False
        
        return True
            
        