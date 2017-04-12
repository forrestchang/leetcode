class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower():
            return True
        elif word.isupper():
            return True
        elif word[0].isupper():
            if word[1:].islower():
                return True
            else:
                return False
        else:
            return False

if __name__ == '__main__':
    assert Solution().detectCapitalUse('USA') == True
    assert Solution().detectCapitalUse('leetcode') == True
    assert Solution().detectCapitalUse('Google') == True
    assert Solution().detectCapitalUse('fUck') == False

