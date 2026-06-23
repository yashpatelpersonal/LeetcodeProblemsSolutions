class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1  # number of possible values
        dp_up = [0] * m
        dp_down = [0] * m
        for j in range(m):
            dp_up[j] = j
            dp_down[j] = (m - 1 - j)
        if n == 2:
            return (sum(dp_up) + sum(dp_down)) % MOD
        # For lengths 3..n
        for _ in range(3, n + 1):
            prefix_down = [0] * (m + 1)
            for j in range(m):
                prefix_down[j + 1] = (prefix_down[j] + dp_down[j]) % MOD
            # suffix sums of dp_up for down transition
            suffix_up = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                suffix_up[j] = (suffix_up[j + 1] + dp_up[j]) % MOD
            new_up = [0] * m
            new_down = [0] * m
            for j in range(m):
                # up: sum of down over u < v  -> indices < j
                new_up[j] = prefix_down[j]  # sum dp_down[0..j-1]
                # down: sum of up over u > v -> indices > j
                new_down[j] = suffix_up[j + 1]  # sum dp_up[j+1..m-1]
            dp_up, dp_down = new_up, new_down
        return (sum(dp_up) + sum(dp_down)) % MOD