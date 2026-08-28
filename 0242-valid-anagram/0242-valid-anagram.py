class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = {}
        hasht = {}
        is_anagram = True

        for letters in s:
            if letters not in hashs:
                hashs[letters] = 1
            else:
                hashs[letters] += 1

        for lettert in t:
            if lettert not in hasht:
                hasht[lettert] = 1
            else:
                hasht[lettert] += 1
        
        if hashs != hasht:
            is_anagram = False
    
        return is_anagram

        