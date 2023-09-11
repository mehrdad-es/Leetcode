def trap(self, height: list[int]) -> int:
    if not height:
        return 0

    l, r = 0, len(height) - 1
    left_max, right_max = height[l], height[r]
    water_trapped = 0
    while l < r:
        if left_max < right_max:
            l += 1
            left_max = max(left_max, height[l])
            water_trapped += left_max - height[l]
        else:
            r -= 1
            right_max = max(right_max, height[r])
            water_trapped += right_max - height[r]
        print(f'{l},{r}-a,b and leftmax,rightmax ({left_max},{right_max}), water trapped: {water_trapped}')
    return water_trapped