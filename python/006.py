class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<2: return s
        res = ["" for row in range(numRows)]
        i = 0
        flag = -1
        for c in s:
            res[i] += c
            if i==0 or i == numRows-1:flag = -flag
            i += flag
        news = ''
        for i in range(numRows):
            news = news + res[i]
        return news
    
s = "PAYPALISHIRING"
n = 3
result = Solution()
print(result.convert(s, n))