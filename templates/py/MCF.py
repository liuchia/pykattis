class MinCostFlow:
	def __init__(self, Capacity, Cost, source, target):
		self.Cost, self.Capacity = Cost, Capacity
		self.n = n = len(Cost)
		self.Parent = Parent = [0 for i in range(n)]
		self.Pi = Pi = [0 for i in range(n)]
		self.Flow = Flow = [[0 for i in range(n)] for j in range(n)]
		totalFlow = totalCost = 0
		while self.search(source, target):
			x, amount = target, 8<<50
			while x != source:
				y = Parent[x]
				newAm = Flow[x][y] if Flow[x][y] != 0 else Capacity[y][x] - Flow[y][x]
				amount = min(amount, newAm)
				x = y
			x = target
			while x != source:
				y = Parent[x]
				if Flow[x][y] != 0:
					Flow[x][y] -= amount
					totalCost -= amount * Cost[x][y]
				else:
					Flow[y][x] += amount
					totalCost += amount * Cost[y][x]
				x = y
			totalFlow += amount
		self.maxflow, self.mincost = totalFlow, totalCost
	def search(self, source, target):
		n,Pi,Cost,Parent,Capacity,Flow = self.n,self.Pi,self.Cost,self.Parent,self.Capacity,self.Flow
		Found = [False for i in range(n+1)]
		Dist = [8<<50 for i in range(n+1)]
		Dist[source] = 0
		while source != n:
			best = n
			Found[source] = True
			for k in range(n):
				if Found[k]: continue
				if Flow[k][source] != 0:
					val = Dist[source] + Pi[source] - Pi[k] - Cost[k][source]
					if Dist[k] > val: Dist[k], Parent[k] = val, source
				if Flow[source][k] < Capacity[source][k]:
					val = Dist[source] + Pi[source] - Pi[k] + Cost[source][k]
					if Dist[k] > val: Dist[k], Parent[k] = val, source
				if Dist[k] < Dist[best]: best = k
			source = best
		for k in range(n): Pi[k] = min(Pi[k] + Dist[k], 8<<50)
		return Found[target]
