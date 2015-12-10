import numpy as np
import random
class Perceptron(object):
	def __init__(self, X, Y, step):
		self.X = self.add_x0(X)
		self.Y = Y
		self.step = step
		c = self.X.shape[1]
		self.w = np.zeros(c).reshape(c, 1)
		self.ERROR = []
		self.iter_count = 0
		self.run()

	def add_x0(self, X):
		r = np.array(X).shape[0]
		b = np.ones(r).reshape(r, 1)
		return np.hstack((b, X))	

	def pp(self):
		self.ERROR = []
		rY = np.dot(self.X, self.w)
		print 'rY', rY
		mY = self.Y * rY > 0
		print 'mY', mY
		self.ERROR = np.where(mY == False)[0]

	def run(self):
		end = False
		while not end and self.iter_count <= 1000:
			self.pp()
			print 'error', self.ERROR
			if len(self.ERROR):
				rand_rownum = random.choice(self.ERROR)
				print 'pick num', rand_rownum
				x = self.X[rand_rownum].reshape(self.X.shape[1], 1)
				y = self.Y[rand_rownum]
				print 'x, y', x, y
				self.w = self.w + self.step * y * x
				self.iter_count += 1
			else:
				end = True

if __name__ == '__main__':
	X = [
		[3, 3, 5],
		[4, 3, 4],
		[1, 1, 2]
	]
	Y = [
		[1],
		[1],
		[-1]
	]
	a = Perceptron(X, Y, 1)
	print 'w', a.w
	print 'iter_count', a.iter_count




