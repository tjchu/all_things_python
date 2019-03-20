class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

def dfs(graph, start, visited = None):
	if visited is None:
		visited = set()
	visited.add(start)
	print(start)
	for next in graph[start] - visited:
		dfs(graph, next, visited)
	return visited


import collections
def bfs(graph, startnode):
	# Track the visited and unvisited nodes using queue
	seen = set([startnode])
	queue = collections.deque([startnode])
	while queue:
		vertex = queue.popleft()
		print(vertex)
		for node in graph[vertex]:
			if node not in seen:
				seen.add(node)
				queue.append(node)


# The graph dictionary
gdict = { 
			"a" : set(["b","c"]),
			"b" : set(["a", "d"]),
			"c" : set(["a", "d"]),
			"d" : set(["e"]),
			"e" : set(["a"])
		}
print("DFS: ")
dfs(gdict, "a")
print("------")
print("BFS: ")
bfs(gdict, "a")