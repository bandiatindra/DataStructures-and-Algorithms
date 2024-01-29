class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        import heapq as hq

        graph = [[] for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        max_prob = [0.0]*n
        max_prob[start_node] = 1.0

        priority_queue = [(-1.0,start_node)]

        while len(priority_queue)!= 0:
            curr_prob, curr_node = hq.heappop(priority_queue)

            if curr_node == end_node:
                return -curr_prob
            for i in range(len(graph[curr_node])):
                if max_prob[graph[curr_node][i][0]] < -curr_prob * graph[curr_node][i][1]:
                    max_prob[graph[curr_node][i][0]] = -curr_prob * graph[curr_node][i][1]
                    hq.heappush(priority_queue, (-max_prob[graph[curr_node][i][0]],graph[curr_node][i][0]))
        return 0.0




    
