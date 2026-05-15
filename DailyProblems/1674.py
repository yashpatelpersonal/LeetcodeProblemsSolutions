class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        for i in range(n // 2):

            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            pair_sum = a + b

            # initially assume 2 moves
            diff[2] += 2

            # one move range
            diff[low] -= 1
            diff[high + 1] += 1

            # zero move at exact sum
            diff[pair_sum] -= 1
            diff[pair_sum + 1] += 1
    
        ans = float('inf')
        current = 0

        for target in range(2, 2 * limit + 1):
            current += diff[target]
            ans = min(ans, current)
        return ans

# if __name__ == '__main__':
#     s = Solution()
#     ans = s.minMoves(nums=[1,2,1,2],limit=2)
#     print(ans)