class Solution:
    def __init__(self):
        self.left: int = 0
        self.right: int = 0
        self.maxlength: int = 0

    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            self.extend(s, i, i)
            self.extend(s, i, i+1)
        return s[int(self.left): int(self.left + self.maxlength)]
    
    def extend(self, s, i: int, j: int):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            if  j - i + 1 > self.maxlength:
                self.left = i
                self.right = j
                self.maxlength = j - i  + 1
            i -= 1
            j += 1
        
        



s = "babad"
result = Solution()
print(result.longestPalindrome(s))