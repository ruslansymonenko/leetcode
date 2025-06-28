class Solution:
    def isPalindrome(self, x: int) -> bool:
        number_to_string = str(x)
        reversed_string = number_to_string[::-1]

        if number_to_string == reversed_string:
            return True

        return False

solution = Solution()

print(solution.isPalindrome(121))