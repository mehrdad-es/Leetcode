def hoursToFinish(self,piles,k):
    res=0
    for n in piles:
        res+=n//k + (n%k > 0)
    return res
def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r
        while l<=r:
            k = l-1+(r-l+1)//2+(r-l+1)%2
            if self.hoursToFinish(piles,k)>h:
                l=k+1
            else:
                r=k-1
                res=k
        return res
