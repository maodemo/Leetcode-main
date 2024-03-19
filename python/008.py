class Solution:
    def myAtoi(self, s: str) -> int:
        num: int = 1
        numstr = ''
        numlist = set(str(i) for i in range(10))
        numlist.update({' ', '-', '+'})
        for i in s:
            if i in numlist:
                if i == ' ':
                    continue
                elif i == '+':
                    numlist = set(str(i) for i in range(10))
                elif i == '-':
                    numlist = set(str(i) for i in range(10))
                    num = -1
                else:
                    numlist = set(str(i) for i in range(10))
                    numstr = numstr + i
            else:
                break
        if numstr == '':
            numstr = 0
        num = num * int(numstr)
        return self.RegionNum(num)


    def RegionNum(self, num) -> int:
        if num < - (2 ** 31):
            return( - (2 ** 31))
        elif num > 2 ** 31 - 1:
            return(2 ** 31 - 1)
        else:
            return(num)
        

    
x = "00000-42a1234"
result = Solution()
print(result.myAtoi(x))