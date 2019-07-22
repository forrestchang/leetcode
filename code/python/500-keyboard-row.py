class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def _check(word, lines):
            word_set = set(word.lower())
            for line in lines:
                word = list(word_set)
                if word[0] in line:
                    for c in word[1:]:
                        if c not in line:
                            return False
                    return True

        line1 = 'qwertyuiop'
        line2 = 'asdfghjkl'
        line3 = 'zxcvbnm'
        lines = [line1, line2, line3]
        result = []
        for word in words:
            if _check(word, lines):
                result.append(word)
        return result

if __name__ == '__main__':
    assert Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
