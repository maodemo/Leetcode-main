class Solution:
    def reverse(self, x: int) -> int:
        y = [1, -1][x < 0] * int(str(abs(x))[::-1])
        return y if y.bit_length() < 32 else 0
    
x = 123
result = Solution()
print(result.reverse(x))