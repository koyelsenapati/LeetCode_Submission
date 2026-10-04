class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""
        base = strs[0]

        for i in range(len(base)):
            for words in strs[1:]:
                if i >= len(words) or words[i] != base[i]:
                    break
            else:
                result += base[i]
                continue

            break

        return result