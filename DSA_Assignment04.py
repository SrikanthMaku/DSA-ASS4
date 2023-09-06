#1

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def breadth_first_traversal(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            print(node, end=' ')
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)


print("Breadth First Traversal starting from node 2:")
g.breadth_first_traversal(2)




# 2

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, node, visited):
        visited[node] = True
        print(node, end=" ")

        if node in self.graph:
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    self.dfs(neighbor, visited)

    def dfs_traversal(self, start_node):
        visited = {node: False for node in self.graph}
        self.dfs(start_node, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth First Traversal starting from node 2:")
g.dfs_traversal(2)


# 3

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_nodes_at_level(root, target_level):
    if not root:
        return 0

    queue = deque([(root, 0)])
    count = 0

    while queue:
        node, level = queue.popleft()
        if level == target_level:
            count += 1
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return count


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

target_level = 2
result = count_nodes_at_level(root, target_level)
print("Number of nodes at level", target_level, ":", result)


# 4

def count_trees(adj_list):
    visited = set()
    count = 0
    
    def dfs(node):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    for node in adj_list:
        if node not in visited:
            count += 1
            dfs(node)
    
    return count

adj_list = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2, 5],
    5: [4]
}

num_trees = count_trees(adj_list)
print("Number of trees in the forest:", num_trees)


# 5

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.isCyclicUtil(neighbor, visited, recStack):
                    return True
            elif recStack[neighbor]:
                return True
        
        recStack[v] = False
        return False
    
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        
        for node in range(self.V):
            if not visited[node]:
                if self.isCyclicUtil(node, visited, recStack):
                    return True
        return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


if g.isCyclic():
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")




