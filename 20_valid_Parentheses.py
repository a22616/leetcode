class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len_s = len(s)
        dicts = {')':'(','}':'{',']':'['}
        opning = '({['
        closing = ')}]'
        lis = []
        if len_s == 0:
            return True
        for char in s:
            if char in opning:
                lis.append(char)
            elif char in closing:
                if len(lis) == 0:
                    return False
                if lis[-1] == dicts[char]:
                    lis.pop()
                else:
                    return False
        return len(lis)==0
        