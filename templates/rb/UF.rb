class UF
	attr_accessor :parent, :height
	def initialize(n)
		@parent = Array.new(n) {|i| i}
		@height = Array.new(n, 0)
	end
	def find(i)
		return i if @parent[i] == i
		@parent[i] = find(@parent[i])
		return @parent[i]
	end
	def connected(i, j)
		return find(i) == find(j)
	end
	def union(i, j)
		if !connected(i, j)
			x, y = find(i), find(j)
			if @height[x] > @height[y]
				@parent[y] = x
			else
				@parent[x] = y
				@height[y] += 1 if @height[x] == @height[y]
			end
		end
	end
end
