class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
                
        graph = defaultdict(list)

        in_degree = [0 for i in range(numCourses)]

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest]+=1
        
        queue = deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        order = []

        while queue:
            elem = queue.popleft()
            order.append(elem)
            
            for neighbor in graph[elem]:
                in_degree[neighbor] -=1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        print(order)
        if len(order) != numCourses:
            return []
        else:
            return order