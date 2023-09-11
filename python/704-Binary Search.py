def search(self, nums: List[int], target: int) -> int:
    l,r=0,len(nums)
    if len(nums)==1:
        if target==nums[0]:
            return 0
        else:
            return -1
    else:
        while l<=r:
            mid = l-1+(r-l+1)//2 + (r-l+1)%2
            if nums[mid]==target:
                return mid
            else:
                if l==mid or r==mid:
                    break
                if nums[mid]<target:
                    l=mid
                elif nums[mid]>target:
                    r = mid
        return -1