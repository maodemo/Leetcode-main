class Solution:
    def myAtoi(self, s: str) -> int:
        sint = ''
        intnum : int = 1
        i = 0
        nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        for i in range(len(s)):
            if s[i] in nums:     
                sint = sint + s[i]
            elif s[i] == '-':
                intnum = -1
        return intnum * int(sint)
    
x = "words and 987"
result = Solution()
print(result.myAtoi(x))