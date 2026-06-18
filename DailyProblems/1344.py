
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        angle = abs(30 * hour - 5.5 * minutes)
        return min(angle, 360 - angle)