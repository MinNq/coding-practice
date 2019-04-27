# data is a table of datapoints, 
#e.g. for 3 datapoints (1,2,3), (1,4,5), (2,6,5) we have:
#	1	2	3
#	1	4	5	
#	2	6	5

import matplotlib.pyplot as plt
import numpy as np

def squared_norm(object1, object2):
	return np.dot(object1 - object2, object1 - object2)
def nearest(object1, objectlist):
	nearest_so_far = 0
	for index in range(len(objectlist)):
		if (squared_norm(object1, objectlist[index]) < squared_norm(object1, objectlist[nearest_so_far])):
			nearest_so_far = index
	return nearest_so_far
def probability(array):
  return array/sum(array)

class KMeans:

  def __init__(self, n_cluster, max_iteration, method = "kmeans++"):
      
    self.n_cluster = n_cluster
    self.max_iteration = max_iteration
    self.corresponding_centroid = []
    self.method = method

  def train(self, data):

		#Choose n_cluster centroids from given datapoints
    
    self.centroids = []
    self.size = data.shape[0]
    
    #with a uniform distribution
    
    if self.method == "vanilla":
      array = np.arange(self.size)
      np.random.shuffle(array)
      for index in range(self.n_cluster):
        self.centroids.append(data[int(array[index])])
    
    #using k-means++
    
    if self.method == "kmeans++":
      self.centroids.append(data[np.random.randint(0, self.size)])
      centroid_count = 1
      while centroid_count < self.n_cluster:
        distribution = []
        for point in data:
          distribution.append(squared_norm(point, self.centroids[nearest(point, self.centroids)]))
        self.centroids.append(data[np.random.choice(range(0, self.size), p = probability(distribution))])
        centroid_count += 1
      
		#Training

    for iteration in range(self.max_iteration):

		#assign each datapoint to the nearest centroid
    
      for index in range(self.size):
        self.corresponding_centroid.append(nearest(data[index], self.centroids))

        
		#calculate new centroid for each cluster
    
      for index in range(self.n_cluster):
        add = np.zeros(data.shape[1])
        count = 0
        for indice in range(self.size):
          if self.corresponding_centroid[indice] == index :
            add += data[indice]
            count += 1
        self.centroids[index] = add/count 
      print("Iteration", iteration + 1,"finished.")
    print("Training completed.")
    
    
  def plot(self, data):
    count = 0
    for item in self.centroids:
      temp = np.array([self.centroids[count]])
      for indice in range(self.size):
        if self.corresponding_centroid[indice] == count:
          temp = np.append(temp,[data[indice]], axis = 0)  
      count += 1
      plt.scatter(temp[1:,0],temp[1:,1], alpha = .7)
      
