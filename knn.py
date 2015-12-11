import numpy as np

class KNN(object):
	def __init__(self, X, Y, k, p):
		self.k = k
		self.p = p
		self.X = X
		self.Y = Y

	def run(self, x):
		indices = self.find_near_k_direct(x)
		near_k_classes = {}
		for i in indices:
			near_k_classes[i] = near_k_classes.setdefault(i, 0) + 1
		return sorted(near_k_classes.items(), key=lambda x: x[0], reverse=True)[0][0]

	def find_near_k_direct(self, x):
		distance_index = []
		for index, ix in enumerate(self.X):
			distance_index.append((self.get_distance(ix, x), index))
		sorted_di = sorted(distance_index, key=lambda x: x[0])
		return [x[1] for x in sorted_di[:self.k]]

	def get_distance(self, ax, bx):
		sum = 0
		for a, b in zip(ax, bx):
			sum += (abs(a -b )) ** self.p
		return sum ** (1.0 / self.p)

if __name__ == '__main__':
	X = [
	[2,3],
	[5,4],
	[9,6],
	[4,7],
	[8,1],
	[7,2]
	]
	Y = [
	1,
	2,
	3,
	4,
	5,
	6,
	]
	knn = KNN(X, Y, k=1, p=2)
	print knn.run([1,1])

