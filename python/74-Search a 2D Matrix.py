def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    l,r = 0,len(matrix)
    while l<=r:
        mid = l-1+(r-l+1)//2 + (r-l+1)%2
        if self.search(matrix[mid],target):
            return True
        else:
            if l==mid or r==mid:
                break
            if matrix[mid][-1]<target:
                l=mid
            elif matrix[mid][0]>target:
                r = mid
            else:
                return False
    return False