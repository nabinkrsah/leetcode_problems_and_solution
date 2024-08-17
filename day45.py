'''2045. Second Minimum Time to Reach Destination
Solved
Hard
Topics
Companies
Hint
A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.

Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.

The second minimum value is defined as the smallest value strictly larger than the minimum value.

For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.

Notes:

You can go through any vertex any number of times, including 1 and n.
You can assume that when the journey starts, all signals have just turned green.
 

Example 1:

       
Input: n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5
Output: 13
Explanation:
The figure on the left shows the given graph.
The blue path in the figure on the right is the minimum time path.
The time taken is:
- Start at 1, time elapsed=0
- 1 -> 4: 3 minutes, time elapsed=3
- 4 -> 5: 3 minutes, time elapsed=6
Hence the minimum time needed is 6 minutes.

The red path shows the path to get the second minimum time.
- Start at 1, time elapsed=0
- 1 -> 3: 3 minutes, time elapsed=3
- 3 -> 4: 3 minutes, time elapsed=6
- Wait at 4 for 4 minutes, time elapsed=10
- 4 -> 5: 3 minutes, time elapsed=13
Hence the second minimum time is 13 minutes.      
Example 2:


Input: n = 2, edges = [[1,2]], time = 3, change = 2
Output: 11
Explanation:
The minimum time path is 1 -> 2 with time = 3 minutes.
The second minimum time path is 1 -> 2 -> 1 -> 2 with time = 11 minutes.'''



from collections import deque, defaultdict
import heapq

class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        pq = [(0, 1, 0)]
        times = defaultdict(lambda: [float('inf'), float('inf')])
        times[1][0] = 0
        visited = set()
        while pq:
            current_time, node, time_reached = heapq.heappop(pq)
            
            if (node, time_reached) in visited:
                continue
            visited.add((node, time_reached))
            cycle = 2 * change
            if (current_time // change) % 2 == 1:
                current_time += change - (current_time % change)
                
            for neighbor in graph[node]:
                new_time = current_time + time
                
                if new_time < times[neighbor][0]:
                    times[neighbor][1] = times[neighbor][0]
                    times[neighbor][0] = new_time
                    heapq.heappush(pq, (new_time, neighbor, new_time))
                elif times[neighbor][0] < new_time < times[neighbor][1]:
                    times[neighbor][1] = new_time
                    heapq.heappush(pq, (new_time, neighbor, new_time))
        
        return times[n][1]
