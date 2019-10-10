class UF:
	def __init__(self, n):
		self.parent = [i for i in range(n)]
		self.height = [0 for i in range(n)]
	def find(self, i):
		if self.parent[i] == i:
			return i
		else:
			self.parent[i] = self.find(self.parent[i])
			return self.parent[i]
	def connected(self, i, j):
		return self.find(i) == self.find(j)
	def union(self, i, j):
		if not self.connected(i, j):
			x, y = self.find(i), self.find(j)
			if self.height[x] > self.height[y]:
				self.parent[y] = x
			else:
				self.parent[x] = y
				if self.height[x] == self.height[y]:
					self.height[y] += 1
