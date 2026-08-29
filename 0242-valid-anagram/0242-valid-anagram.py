class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = {}

        for letterS in s:
            count[letterS] = count.get(letterS, 0) + 1
        for letterT in t:
            count[letterT] = count.get(letterT, 0) - 1

        for v in count.values():
            print(v == 0)

        return all(v == 0 for v in count.values())