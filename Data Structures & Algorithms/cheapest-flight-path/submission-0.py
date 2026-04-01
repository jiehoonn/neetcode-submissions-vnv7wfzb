import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build Graph
        graph = {i: {} for i in range(n)}
        for u, v, w in flights:
            graph[u][v] = w
        
        # distances[node] = (min_cost, stops_taken)
        # We need to track stops because a more expensive path might have fewer stops
        stop_limits = {i: float('inf') for i in range(n)}
        
        # queue stores (cost, current_node, stops)
        queue = [(0, src, 0)]

        while queue: 
            current_distance, current_node, stops = heapq.heappop(queue) 
    
            if current_node == dst:
                return current_distance
            
            if stops > k or stops >= stop_limits[current_node]:
                continue
            
            stop_limits[current_node] = stops
    
            for neighbor, weight in graph[current_node].items(): 
                heapq.heappush(queue, (current_distance + weight, neighbor, stops + 1))
        
        return -1