#暴力穷举法

# def seen_characters(input_str: str):
#     seen_characters = set()
#     for char in input_str:
#         if char in seen_characters:
#             return True
#         seen_characters.add(char)
#     return False

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if s == "":
#             return 0
#         for i in range(1, len(s)+1):
#             for j in range(len(s) - i + 1):
#                 if seen_characters(s[j: j+i]) == False:
#                     num = i
#         return num   

#哈希表
class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        max_length = 0
        char_count = {}
        right, left = 0, 0
        while right < len(s):
            if s[right] in char_count and char_count[s[right]] > 0:
                char_count.clear()                
                left += 1
                right =left
            else:
                char_count[s[right]] = 1
                max_length = max(right - left + 1, max_length)
                right += 1
        return max_length
    
s = "dvdf"
result = Solution.lengthOfLongestSubstring(s)
print(result)
