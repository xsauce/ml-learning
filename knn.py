import numpy as np

class KNN(object):
	def __init__(self, X, Y, k, p):
		self.k = k
		self.p = p
		self.X = np.array(X)
		self.Y = np.array(Y)

	def run(self, x):
		indices = self.find_near_k_direct(x)
		near_k_classes = {}
		for i in indices:
			lb = self.Y[i]
			near_k_classes[lb] = near_k_classes.get(lb, 0) + 1
		print near_k_classes
		return sorted(near_k_classes.items(), key=lambda x: x[1], reverse=True)[0][0]

	def find_near_k_direct(self, x):
		diffmat = np.tile(x, (self.X.shape[0], 1)) - self.X
		sqdiffmat = diffmat ** self.p
		sqdistances = sqdiffmat.sum(axis=1)
		distances = sqdistances ** 0.5
		sorted_distance_indices = distances.argsort()
		print sorted_distance_indices
		return sorted_distance_indices[:self.k]

if __name__ == '__main__':
	X = [
	[2,3],
	[2,1],
	[2,0],
	[3,1],
	[8,2],
	[7,2]
	]
	Y = [
	'A',
	'B',
	'A',
	'C',
	'E',
	'F',
	]
	knn = KNN(X, Y, k=6, p=2)
	print knn.run([1,1])

