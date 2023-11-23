class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        if len(xstr) % 2 ==0:
            self.lookBoolNum(xstr, int(len(xstr) / 2))
        if len(xstr) % 2 == 1:
            self.lookBoolNum(xstr, int((len(xstr) - 1) / 2))
        return self.boolnum
            

    def lookBoolNum(self, xstr, num):
        if num == 0:
            self.boolnum = True
        for i in range(num):
            if xstr[i] == xstr[-1 - i]:
                self.boolnum = True
            else:
                self.boolnum = False
                break

x = 00
result = Solution()
print(result.isPalindrome(x))