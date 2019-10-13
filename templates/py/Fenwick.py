class Fenwick:
	def __init__(self, n):
		self.size = n
		self.tree = [0 for i in range(n+1)]
	def update(self, index, value):
		while index <= self.size:
			self.tree[index] += value
			index += index & -index
	def query(self, index):
		total = 0
		while index > 0:
			total += self.tree[index]
			index -= index & -index
		return total
