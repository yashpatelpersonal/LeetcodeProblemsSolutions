from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        # ---------------------------------------------------------
        # 1. Multi-source BFS to compute distance to nearest thief
        # ---------------------------------------------------------
        dist = [[10**9] * n for _ in range(n)]
        q = deque()

        for r in range(n):
            row = grid[r]
            for c in range(n):
                if row[c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            base = dist[r][c] + 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] > base:
                    dist[nr][nc] = base
                    q.append((nr, nc))

        # ---------------------------------------------------------
        # 2. BFS check for safeness >= k
        # ---------------------------------------------------------
        def can(k):
            if dist[0][0] < k:
                return False

            q = deque([(0,0)])
            seen = [[False]*n for _ in range(n)]
            seen[0][0] = True

            while q:
                r, c = q.popleft()
                if r == n-1 and c == n-1:
                    return True

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                            0 <= nr < n and 0 <= nc < n and
                            not seen[nr][nc] and
                            dist[nr][nc] >= k
                    ):
                        seen[nr][nc] = True
                        q.append((nr, nc))

            return False

        # ---------------------------------------------------------
        # 3. Binary search for maximum safeness factor
        # ---------------------------------------------------------
        hi = max(max(row) for row in dist)
        lo, ans = 0, 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
