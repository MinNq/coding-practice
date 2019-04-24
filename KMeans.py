# data is a table of datapoints, 
#e.g. for 3 datapoints (1,2,3), (1,4,5), (2,6,5) we have:
#	1	2	3
#	1	4	5	
#	2	6	5


import numpy as np

def norm(object1, object2):
	return np.dot(object1 - object2, object1 - object2)
def nearest(object1, objectlist):
	nearest_so_far = 0
	for index in range(len(objectlist)):
		if (norm(object1, objectlist[index]) < norm(object1, objectlist[nearest_so_far])):
			nearest_so_far = index
	return nearest_so_far

class KMeans:

	def __init__(self, n_cluster, max_iteration):
		self.n_cluster = n_cluster
		self.max_iteration = max_iteration

	def train(self, data):

		#randomly choose n_cluster centroids from given datapoints
		self.centroids = []
		self.size = data.shape[0]
		array = np.arange(self.size)
		np.random.shuffle(array)
		for index in range(self.n_cluster):
			self.centroids.append(data[int(array[index])])		

		centroid_list = []
		for index in range(self.size):
			centroid_list.append(0)

		#Training

		for iteration in range(self.max_iteration):

		#assign each datapoint to the nearest centroid
			for index in range(self.size):
				centroid_list[index] = nearest(data[index], self.centroids)

		#calculate new centroid for each cluster
			for index in range(self.n_cluster):
				add = np.zeros(data.shape[1])
				count = 0
				for indice in range(self.size):
					if centroid_list[indice] == index :
						add += data[indice]
						count += 1
				self.centroids[index] = add/count 
			print("Iteration ", iteration + 1,"th finished.")
		print("Training completed.")