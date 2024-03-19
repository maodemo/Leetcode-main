class Solution:
    def romanToInt(self, s: str) -> int:
        num: int = 0
        lonenum = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 
        }
        twicenum = {
            'IV': -2, 'IX': -2, 'XL': -20, 'XC': -20, 'CD': -200, 'CM': -200 
        }
        for i in range(len(s)):
            num = num + lonenum[s[i]]
        for j in range(len(s) - 1):
            if s[j: j + 2] in twicenum.keys():
                num = num + twicenum[s[j: j + 2]]
        return num

x = "MCMXCIV"
result = Solution()
print(result.romanToInt(x))