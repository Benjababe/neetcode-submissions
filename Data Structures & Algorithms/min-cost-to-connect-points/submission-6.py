from queue import PriorityQueue

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        
        visited = set()
        total_dist = 0

        points = [(p[0], p[1]) for p in points]

        islands = {}
        for i in range(len(points)):
            islands[points[i]] = f"{i}"

        pq = PriorityQueue()
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                pq.put((dist, points[i], points[j]))

        edges_sel = 0
        while not pq.empty() or edges_sel < (len(points) - 1):
            dist, p1, p2 = pq.get()

            if islands[p1] == islands[p2]:
                continue

            to_change = islands[p2]
            for k, v in islands.items():
                if v == to_change:
                    islands[k] = islands[p1]

            total_dist += dist
            visited.add(p1)
            visited.add(p2)
            edges_sel += 1

        print(islands)
        return total_dist