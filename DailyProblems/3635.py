class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)

        # Find the absolute earliest independent finish times
        min_land_finish = float('inf')
        for i in range(n):
            min_land_finish = min(min_land_finish, landStartTime[i] + landDuration[i])

        min_water_finish = float('inf')
        for j in range(m):
            min_water_finish = min(min_water_finish, waterStartTime[j] + waterDuration[j])

        ans = float('inf')

        # Strategy 1: Land Ride first, then Water Ride
        # We pair the earliest finishing land ride with every possible water ride
        for j in range(m):
            finish = max(min_land_finish, waterStartTime[j]) + waterDuration[j]
            if finish < ans:
                ans = finish

        # Strategy 2: Water Ride first, then Land Ride
        # We pair the earliest finishing water ride with every possible land ride
        for i in range(n):
            finish = max(min_water_finish, landStartTime[i]) + landDuration[i]
            if finish < ans:
                ans = finish

        return ans