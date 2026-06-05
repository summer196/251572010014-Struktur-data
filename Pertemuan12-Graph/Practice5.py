#Search DFS

class Graph:
    def __init__(self):
        self.graph = {
            "A": ["B"],
            "B": ["A", "C"],
            "C": ["B"]
        } 
    def search(self, start, goal):
        visited = set()
        def dfs(v):
            if v == goal:
                return True
            visited.add(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(start)
    
g = Graph()
print("A ke C?", g.search("A", "C"))
print("A ke B?", g.search("A", "B"))
print("B ke C?", g.search("B", "C"))
print("A ke D?", g.search("A", "D"))