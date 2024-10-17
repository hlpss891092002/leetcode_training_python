from typing import List
def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = dict() # Found dict, key is node value, value are list that record all neighbor node 
        for edge in edges:
            u, i =  edge
            if u not in graph :
                graph[u] = [] 
                graph[u].append(i)
            else:
                graph[u].append(i)     
            if i not in graph :
                graph[i] = []
                graph[i].append(u)
            else:
                graph[i].append(u)     
        def traverse_node(node, visited): # build a recursion function 
            if destination == node: # found destination
                return True
            else:
                visited.add(node) # recording the nodes were visited with set , to avoid duplicate records
                for i in  graph[node]: # iterate neighbor node
                    if i not in visited: # visit the node that unvisited
                        if traverse_node(i, visited): # found 
                            return True
            return False # there is no destination in graph of source. 
        visited = set()
        return traverse_node(source, visited)