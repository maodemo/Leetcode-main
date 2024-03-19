class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
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
result = Solution()
print(result.findMedianSortedArrays(nums1, nums2))