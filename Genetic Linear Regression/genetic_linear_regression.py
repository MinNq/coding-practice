# data is a table where each row contains a scalar output and a vector-valued input
# e.g., if data is
# 6.0   1.4   4.5   5.3
# 4.9   2.9   7.3   6.0
# then 6.0 and 4.0 are outputs
# and n_weights = 3 (weights) + 1 (bias)


import numpy as np
import matplotlib.pyplot as plt

def loss(weights, data):
  
  one = np.transpose(np.array([[1]*np.shape(data)[0]]))
  augmented_data = np.append(data, one, axis = 1)
  iro = data[:,0] - np.dot(augmented_data[:,1:], weights)
  
  return np.dot(iro, iro)

def offsprings(parent1, parent2):
  
  cut = np.random.randint(1,np.size(parent1))
  
  child1 = []
  child2 = []
  for count in range(cut):
    child1.append(parent1[cut])
    child2.append(parent2[cut])
  for count in range(cut, np.size(parent1)):
    child1.append(parent2[cut])
    child2.append(parent1[cut])
    
  return child1, child2

def mutated(individual, interval):
  mutated_individual = individual
  count = 0
  for feature in individual:
    suitable = np.random.choice([True,False], p = [0.1, 0.9])
    if suitable:
      mutated_individual[count] = (interval[1]-interval[0])*np.random.random_sample() + interval[0]
    count += 1
    
  return mutated_individual

def best(pool, data):
  best_so_far = 0
  count = 0
  for individual in pool:
    if loss(individual, data) < loss(pool[best_so_far], data):
      best_so_far = count
    count += 1
  return loss(pool[best_so_far], data)

class genetic:
  
  def __init__(self, n_weights, crossover_rate = 0.8, mutation_rate = 0.001, population = 1000, max_iteration = 30, interval = [-100,100], adaptive_mutation = True):
    
    self.n_weights = n_weights
    self.crossover_rate = crossover_rate
    self.mutation_rate = mutation_rate
    self.population = population
    self.max_iteration = max_iteration
    self.interval = interval
    self.adaptive_mutation = adaptive_mutation
    
  def train(self, data, training_info = False):
    
    global_best = None
    performance_log = []
    temp_loss = 0
    
    self.initialize()
    for iteration_count in range(self.max_iteration):
        
      self.parents_chosing(data)
      self.crossover()
      self.mutation()
      self.pool = self.newpool
      if training_info:
        print("Gen", iteration_count + 1, "completed.")
        print("Gen's lowest loss:", best(self.pool ,data))
      
      # Performance log for plotting
      
      if global_best == None or best(self.pool, data)< global_best:
        global_best = best(self.pool, data)
      performance_log.append(1/best(self.pool, data))
      
      # adaptive mutation rate
      
      if self.adaptive_mutation:
        if iteration_count > 0:
          if performance_log[iteration_count] > performance_log[iteration_count - 1]:
            self.mutation_rate *= 0.95
          if performance_log[iteration_count] < performance_log[iteration_count - 1]:
            self.mutation_rate /= 0.95
          
    print("Training completed. Lowest loss:", global_best)
    
    plt.plot(range(self.max_iteration), performance_log)
    plt.xlabel('Iteration')
    plt.ylabel('Fitness')
    
    
  def initialize(self):
    
    self.pool = (self.interval[1] - self.interval[0])*np.random.random_sample([self.population, self.n_weights]) + self.interval[0]
  
  def parents_chosing(self, data):
    
    self.population = np.shape(self.pool)[0]
    
    # fitness sorting
    
    fitness_table = []
    
    count = 0
    for individual in self.pool:
      fitness_table.append([loss(individual, data),count])
      count += 1
    
    fitness_table.sort(key = lambda x: x[0], reverse = True)
    
    count = 0
    for item in fitness_table:
      item.append(count)
      count += 1
      
    fitness_table.sort(key = lambda x: x[1])
    
    # rank based parents selection
    
    sigma = self.population*(self.population - 1)//2
    
    distribution = []
    
    for item in fitness_table:
      distribution.append(item[2]/sigma)
      
    markers = np.random.choice(range(self.population), size = self.population - self.population%2, p = distribution )
    
    self.parents = []
    
    for item in markers:
      self.parents.append(self.pool[item])
      
  def crossover(self):
    
    self.newpool = []
    count = 0
    while count < np.shape(self.parents)[0] - np.shape(self.parents)[1]%2:
      suitable = np.random.choice([True, False], p = [self.crossover_rate, 1 - self.crossover_rate])
      if suitable:
        nihon = offsprings(self.parents[count],self.parents[count + 1])
        self.newpool.append(nihon[0])
        self.newpool.append(nihon[1])
      else:
        self.newpool.append(self.parents[count])
        self.newpool.append(self.parents[count + 1])
      count += 2
    
  def mutation(self):
    for individual in self.newpool:
      suitable = np.random.choice([True,False], p = [self.mutation_rate, 1 - self.mutation_rate])
      if suitable:
        individual = mutated(individual, self.interval)
