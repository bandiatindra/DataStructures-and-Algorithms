class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        R1_area = (ax2-ax1) * (ay2-ay1)
        R2_area = (bx2-bx1) * (by2-by1)
        Common_area = 0
        if min(ax2,bx2) > max (ax1, bx1) and min (ay2,by2) > max(ay1, by1):
            Common_area = (min(ax2,bx2) - max (ax1, bx1)) * (min (ay2,by2) - max(ay1, by1))

        Total_area = R1_area + R2_area - Common_area
        return Total_area
