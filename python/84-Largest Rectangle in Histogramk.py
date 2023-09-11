def largestRectangleArea(self, heights: List[int]) -> int:
    m=0
    stack=[]
    for i,h in enumerate(heights):
        start = i
        while stack and stack[-1][1]>h:
            index,height=stack.pop()
            m=max(m,height*(i-index))
            start = index
        stack.append((start,h))
    n = len(heights)
    for i,h in stack:
        m=max(m,h*(n-i))
    return m