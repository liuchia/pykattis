from collections import deque
def shortestAugmentingPath(C, A, F, s, t):
	n, queue = len(C), deque([s])
	P, M = [-1 for i in range(n)], [0 for i in range(n)]
	P[s], M[s] = -2, 10**10
	while queue:
		u = queue.popleft()
		for v in A[u]:
			if C[u][v] - F[u][v] > 0 and P[v] == -1:
				P[v], M[v] = u, min(M[u], C[u][v] - F[u][v])
				if v != t:
					queue.append(v)
				else:
					return M[t], P
	return 0, P

def EdmondsKarp(CapMatrix, AdjList, source, target):
	flow, length = 0, len(CapMatrix)
	FlowMatrix = [[0 for i in range(length)] for j in range(length)]
	while True:
		bottle, Parent = shortestAugmentingPath(CapMatrix, AdjList, FlowMatrix, source, target)
		if bottle == 0:
			break
		flow += bottle
		v = target
		while v != source:
			u = Parent[v]
			FlowMatrix[u][v] += bottle
			FlowMatrix[v][u] -= bottle
			v = u
	return (flow, FlowMatrix)
