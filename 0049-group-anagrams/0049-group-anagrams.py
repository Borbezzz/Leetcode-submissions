class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        temp_arr = []
        final_arr = []

        for word in strs:
            for chrt in word:
                hash[chrt] = hash.get(chrt, 0) + 1
            temp_arr.append((word, hash.copy()))
            hash.clear()

        used = [False] * len(temp_arr)

        for i in range(len(temp_arr)):
            if used[i]:
                continue
            group = [temp_arr[i][0]]
            used[i] = True
            for j in range(len(temp_arr)):
                if i != j and temp_arr[i][1] == temp_arr[j][1]:
                    group.append(temp_arr[j][0])
                    used[j] = True
            final_arr.append(group)

        return final_arr



