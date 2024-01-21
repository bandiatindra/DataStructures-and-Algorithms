class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        import heapq as hq
        adj = [[] for _ in range(n)]
        cost = [[] for _ in range(n)]
        for a, b , w in flights:
            adj[a].append(b)
            cost[a].append(w)

        
        stops = [float('inf')]*n
        
        #stops[src] = 0

        priority_queue = []
        hq.heappush(priority_queue, (0,src,0))
        while len(priority_queue) !=0:
            d, u, steps = hq.heappop(priority_queue)
            if steps > stops[u] or steps > k+1:
                continue
            stops[u] = steps
            if u == dst:
                return d

            for i in range(len(adj[u])):
             
                hq.heappush(priority_queue, (d + cost[u][i],adj[u][i], steps+1))
                
        return -1

        