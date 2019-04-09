class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findMedianOfOddArray(nums1: List[int], nums2: List[int]) -> float:
            mid = ( len(nums1) + len(nums2) + 1) / 2
            pos1 = 0
            pos2 = 0
            count = 0

            while pos1 < len(nums1) and pos2 < len(nums2):
                count += 1
                if nums1[pos1] < nums2[pos2]:
                    if count == mid:
                        return nums1[pos1]
                    pos1 += 1
                else:
                    if count == mid:
                        return nums2[pos2]
                    pos2 += 1

            while pos1 < len(nums1):
                count += 1
                if count == mid:
                    return nums1[pos1]
                pos1 += 1

            while pos2 < len(nums2):
                count += 1
                if count == mid:
                    return nums2[pos2]
                pos2 += 1

        def findMedianOfEvenArray(nums1: List[int], nums2: List[int]) -> float:
            mid = ( len(nums1) + len(nums2)) / 2
            pos1 = 0
            pos2 = 0
            count = 0
            first = 0

            while pos1 < len(nums1) and pos2 < len(nums2):
                count += 1
                if nums1[pos1] < nums2[pos2]:
                    if count == mid:
                        first = nums1[pos1]
                    if count > mid:
                        return ( first + nums1[pos1] ) / 2
                    pos1 += 1
                else:
                    if count == mid:
                        first = nums2[pos2]
                    if count > mid:
                        return ( first + nums2[pos2] ) / 2
                    pos2 += 1

            while pos1 < len(nums1):
                count += 1
                if count == mid:
                    first = nums1[pos1]
                if count > mid:
                    return ( first + nums1[pos1]) / 2
                pos1 += 1

            while pos2 < len(nums2):
                count += 1
                if count == mid:
                    first = nums2[pos2]
                if count > mid:
                    return (first + nums2[pos2]) / 2
                pos2 += 1

        if ( len(nums1) + len(nums2) ) % 2 == 1:
            return findMedianOfOddArray(nums1 = nums1, nums2 = nums2)
        else:
            return findMedianOfEvenArray(nums1 = nums1, nums2 = nums2)
    

        
        
        
        