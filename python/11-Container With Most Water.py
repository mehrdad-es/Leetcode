def maxArea(self, height: list[int]) -> int:
    l,r,curr_max = 0,len(height)-1,0
    while l<r:
        area= (r-l)*min(height[l],height[r])
        # print((height[l],height[r]),((r-l),min(height[l],height[r])),(area,curr_max))
        curr_max= max(area,curr_max)
        if height[r]>height[l]:
            l+=1
        elif height[l]>height[r]:
            r-=1
        else:
            l+=1
    return curr_max