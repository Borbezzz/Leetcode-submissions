class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashS, hashT = {}, {}
        is_anagram = True

        for letterS in s:
            hashS[letterS] = hashS.get(letterS, 0) + 1

        for letterT in t:
            hashT[letterT] = hashT.get(letterT, 0) + 1

        if hashS != hashT:
            is_anagram = False
    
        return is_anagram