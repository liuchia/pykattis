class UF:
	def __init__(self, n):
		self.parent = [i for i in range(n)]
		self.height = [0 for i in range(n)]
	def find(self, i):
		ancestors = []
		while self.parent[i] != i:
			ancestors.append(i)
			i = self.parent[i]
		for x in ancestors:
			self.parent[x] = i
		return i
	def union(self, i, j):
		x, y = self.find(i), self.find(j)
		if x != y:
			if self.height[x] > self.height[y]:
				self.parent[y] = x
			else:
				self.parent[x] = y
				if self.height[x] == self.height[y]:
					self.height[y] += 1
