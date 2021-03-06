class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0 and i % 5 != 0:
                result.append('Fizz')
            elif i % 3 != 0 and i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result

if __name__ == '__main__':
    result = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    assert Solution().fizzBuzz(15) == result
