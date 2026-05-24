class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited=[0]*n
        def dfs(node, out):
            if visited[node] == 0:
                out.append(node)
            else:
                return

            visited[node]=1

            for neighbor in adj[node]:
                dfs(neighbor, visited)

        res=[]
        for i in range(n):
            if visited[i] == 0:
                l=[]
                dfs(i, l)
                res.append(l)
        
        return len(res)