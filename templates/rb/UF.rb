# Needed: n
Parent = Array.new(n) {|i| i}
Height = Array.new(n, 0)

def find(a)
	return a if a == Parent[a]
	Parent[a] = find(Parent[a])
end

def union(a, b)
	ra = find(a)
	rb = find(b)
	if Height[ra] > Height[rb]
		Parent[rb] = ra
	else
		Parent[ra] = rb
		Height[rb] += 1 if Height[ra] == Height[rb]
	end
end

