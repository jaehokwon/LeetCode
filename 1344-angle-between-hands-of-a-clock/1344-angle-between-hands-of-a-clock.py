class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        hoursAngle = (360 * (hour/12)) + (30 * (minutes/60))
        minutesAngle = 360 * (minutes/60)
        result = abs(hoursAngle-minutesAngle)
        result = min(360-result, result)
        return result