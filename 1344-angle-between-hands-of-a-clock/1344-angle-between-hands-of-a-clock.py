class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        hoursAngle = (360 * (hour/12)) + (30 * (minutes/60))
        minutesAngle = 360 * (minutes/60)
        result = min(abs(hoursAngle-minutesAngle), abs(minutesAngle-hoursAngle))
        if result > 180:
            result = 360 - hoursAngle + minutesAngle  if hoursAngle > minutesAngle else 360 - minutesAngle + hoursAngle
        
        return result