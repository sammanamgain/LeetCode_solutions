from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def check(dist_nearest_thief, sf):
            que = deque([(0, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True

            if dist_nearest_thief[0][0] < sf:
                return False

            while que:
                curr_i, curr_j = que.popleft()

                if curr_i == n - 1 and curr_j == n - 1:
                    return True

                for dir_i, dir_j in directions:
                    new_i = curr_i + dir_i
                    new_j = curr_j + dir_j

                    if (
                        0 <= new_i < n
                        and 0 <= new_j < n
                        and not visited[new_i][new_j]
                        and dist_nearest_thief[new_i][new_j] >= sf
                    ):
                        que.append((new_i, new_j))
                        visited[new_i][new_j] = True

            return False

        # Step-1 Precalculation of distNearestThief - for each cell
        dist_nearest_thief = [[-1] * n for _ in range(n)]
        que = deque()
        visited = [[False] * n for _ in range(n)]

        # Push all cells in queue where thieves are present
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    que.append((i, j))
                    visited[i][j] = True

        level = 0
        while que:
            size = len(que)

            for _ in range(size):
                curr_i, curr_j = que.popleft()
                dist_nearest_thief[curr_i][curr_j] = level

                for dir_i, dir_j in directions:
                    new_i = curr_i + dir_i
                    new_j = curr_j + dir_j

                    if (
                        0 <= new_i < n
                        and 0 <= new_j < n
                        and not visited[new_i][new_j]
                    ):
                        que.append((new_i, new_j))
                        visited[new_i][new_j] = True

            level += 1

        # Step-2 Apply binary search on SF
        l, r = 0, 400
        result = 0

        while l <= r:
            mid_sf = (l + r) // 2

            if check(dist_nearest_thief, mid_sf):
                result = mid_sf
                l = mid_sf + 1
            else:
                r = mid_sf - 1

        return result