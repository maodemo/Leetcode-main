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
    def findMedianSortedArrays( nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2 == 0:
            mid = int(len(nums1)/2)
            result = (float(nums1[mid - 1]) + float(nums1[mid]))/2
        else:
            mid = int((len(nums1)+1)/2)
            result = float(nums1[mid - 1])
        return result

nums1 = [1, 3]; nums2 = [2]
result = Solution.findMedianSortedArrays(nums1, nums2)
print(result)