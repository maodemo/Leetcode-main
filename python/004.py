def hebing(nums1, nums2) -> list[int]:
    num = []
    while len(num) <= len(nums1) + len(nums2):
        if nums1[i] < nums2[j]:
            num.append(nums1[i])
            k += 1
            i += 1
        elif nums1[i] > nums2[j]:
            num.append(nums2[j])
            k += 1
            j += 1
        else:
            num.extend([nums2[j], nums2[j]])
            k += 2
            j += 1
            i += 1
    result = (float(num[-1]) + float(num[-2]))/2


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i = 0
        j = 0
        k = 0
        num = []
        if (len(nums1) + len(nums2))%2 == 0:
            result = (float(num[-1]) + float(num[-2]))/2
        else:
            result = float(num[-1])
        return result

nums1 = [1, 3]; nums2 = [2]
result = Solution.lengthOfLongestSubstring(nums1, nums2)
print(result)