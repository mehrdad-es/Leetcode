class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        l,r=0,len(nums1)-1
        total = len(nums1)+len(nums2)
        half = total//2
        while True:
            mid = (r+l)//2
            mid_2 = half-mid-2
            nums1_left=nums1[mid] if mid>=0 else float('-infinity')
            nums1_right=nums1[mid+1] if mid+1<len(nums1) else float('infinity')
            nums2_left=nums2[mid_2] if mid_2>=0 else float('-infinity')
            nums2_right = nums2[mid_2+1] if mid_2+1<len(nums2) else float('infinity')

            if nums1_left<=nums2_right and nums2_left<=nums1_right:
                if total%2:
                    return min(nums1_right,nums2_right)
                return (max(nums1_left,nums2_left)+min(nums1_right,nums2_right))/2
            if nums1_left>nums2_right:
                r=mid-1
            else:
                l=mid+1

        