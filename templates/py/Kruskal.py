# Requires UF
# n for number of vertices
# edges is a list of 3-tuples of (weight, vertexA, vertexB)
from heapq import heappop, heappush
def Kruskal(n, edges):
	groups, edgeGroup = n, UF(n)
	edgeHeap, edgeList = [], []
	for e in edges:
		heappush(edgeHeap, e)
	while groups > 1:
		w, i, j = heappop(edgeHeap)
		if edgeGroup.find(i) != edgeGroup.find(j):
			groups -= 1
			edgeGroup.union(i, j)
			edgeList.append((w, i, j))
	return edgeList
