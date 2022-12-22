class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)  
        # Create a graph
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Store all nodes to be viewed in a queue
        queue = []
        seen = [0]*n
        seen[source] = 1
        queue.append(source)
        while queue:
            curr_node = queue.pop(0)
            seen[curr_node] = 1
            if curr_node == destination:
                return True
            for next_node in graph[curr_node]:
                if seen[next_node] == 0:
                    queue.append(next_node)
                    seen[next_node] = 1

        return False