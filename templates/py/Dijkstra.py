from heapq import heappop, heappush
def dijkstra(adj, s, t):
	# adj is an adjacency list of [Vertex -> (Vertex, Weight)]
	# s is source, t is target
	frontier = [(0.00, s)]
	visited = set()
	while len(frontier) > 0:
		cost, pos = heappop(frontier)
		if pos == t:
			return cost
		if pos not in visited:
			visited.add(pos)
			for neigh, fee in adj[pos]:
				heappush(frontier, (cost+fee, neigh))
	return 9e99
