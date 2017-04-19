class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for char in ransomNote:
            if char not in magazine:
                return False
            else:
                if ransomNote.count(char) > magazine.count(char):
                    return False
        return True


if __name__ == '__main__':
    assert Solution().canConstruct("a", "b") == False
    assert Solution().canConstruct("a", "a") == True
    assert Solution().canConstruct("a", "ab") == True
    assert Solution().canConstruct("aa", "ab") == False
    assert Solution().canConstruct("aa", "aab") == True
    assert Solution().canConstruct("aa", "ab") == False
    assert Solution().canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj") == True
