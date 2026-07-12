class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict, deque

        # Build adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        complete_count = 0

        for start in range(n):
            if visited[start]:
                continue

            # BFS to collect component nodes
            queue = deque([start])
            visited[start] = True
            nodes = {start}
            edge_count = 0

            while queue:
                node = queue.popleft()
                # Count edges from this node
                edge_count += len(graph[node])

                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        queue.append(nei)
                        nodes.add(nei)

            # Each undirected edge counted twice
            edge_count //= 2

            k = len(nodes)
            # Complete graph must have k*(k-1)/2 edges
            if edge_count == k * (k - 1) // 2:
                complete_count += 1

        return complete_count