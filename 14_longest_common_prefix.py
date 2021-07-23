class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        
        min_len = len(strs[0])
        other_str = strs[1:]
        for s in other_str:
            len_s = len(s)
            if min_len > len_s:
                min_len = len_s
                
        c = ""
        k = ""
        for i in range(min_len):
            c = strs[0][i]
            for s in other_str:
                if c != s[i]:
                    c = ""
            if not c:
                break
            k += c
        return k
