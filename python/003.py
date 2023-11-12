#暴力穷举法

def seen_characters(input_str: str):
    seen_characters = set()
    for char in input_str:
        if char in seen_characters:
            return True
        seen_characters.add(char)
    return False

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        for i in range(1, len(s)+1):
            for j in range(len(s) - i + 1):
                if seen_characters(s[j: j+i]) == False:
                    num = i
        return num   