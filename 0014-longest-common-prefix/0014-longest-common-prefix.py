class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        base = strs[0]

        for i in range(len(base)):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or base[i] != strs[j][i]:
                    return base[:i]

        return base