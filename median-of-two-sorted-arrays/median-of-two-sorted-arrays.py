class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = 0
        right = 0
        res = []
        while left < len(nums1) or right < len(nums2):
            if left < len(nums1) and right < len(nums2):
                if nums1[left] < nums2[right]:
                    res.append(nums1[left])
                    left += 1
                else:
                    res.append(nums2[right])
                    right += 1
            elif left < len(nums1):
                res.append(nums1[left])
                left += 1
            else:
                res.append(nums2[right])
                right += 1
        sz = len(res)
        if sz % 2 == 0:
            return (res[sz // 2] + res[sz // 2 - 1]) / 2
        else:
            return res[sz // 2]
        