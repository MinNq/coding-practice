import matplotlib.pyplot as plt 
import numpy as np


def softmax(score_set):
  
  """ activate a score_set of shape (C,1)
  """
  
  score_set = np.exp(score_set - max(score_set))
  
  return score_set / sum(score_set)

  
class softmax_regressor:
  
  def __init__(self, ndim, nclass, max_iter = 50, learning_rate = 0.03):
    
    self.ndim = ndim
    self.nclass = nclass
    
    # Weight matrix initialization
    self.weight = np.random.randn(self.ndim + 1, self.nclass)
    
    self.learning_rate = learning_rate
    self.max_iter = max_iter
  
  
  def train(self, data):
    
    """ Stochastic Gradient Descent:
          Initialize weight matrix (done in __init__)
          While not converged:
            1. Shuffle observations
            2. Update weight with each data point
            3. Repeat
    """
    
    self.loss_log = []
    
    iteration = 0
    
    while iteration < self.max_iter:
      
      iteration += 1
      
      np.random.shuffle(data)
      
      for data_point in data:
        self.update(data_point)
        
      self.loss_log.extend(self.loss())
      print("<Iteration {}> Loss: {}".format(iteration, self.loss()[0][0]))
      
    print('Training completed!')
      
  
  """ data is of shape (n, m + 1),
      in each row:
        first entry is label (e.g. 0, 1, 2, ...)
        the rest is data point of shape (1, m)
  """
  
  def inp(self, data_point):
    
    """ Create augmented data point of shape (m, 1)
    """
    
    point = np.concatenate((data_point, [1]))

    return point[1:].reshape((self.ndim + 1, 1))
  
  
  def label(self, data_point):
    
    """ Create one-hot label of shape (C, 1)
        for a data point
    """
    
    one_hot = np.zeros((self.nclass, 1))  
    one_hot[int(data_point[0])] = 1
    
    return one_hot
    
    
  def update(self, data_point):
    
    difference = self.label(data_point) - self.forward(data_point)
    self.weight += self.learning_rate*np.dot(self.inp(data_point), difference.T)
  
  
  def forward(self, data_point):
    
    """ Compute network's output of shape (C, 1)
    """
    
    score = np.dot(self.weight.T, self.inp(data_point))
    score = softmax(score)
    
    return score
  
  
  def loss(self):
    
    """ For tracking value of loss function
        at each iteration
    """
    
    loss_func = 0
    for data_point in data:
      loss_func -= np.dot(self.label(data_point).T, np.log(softmax(self.forward(data_point))))
      
    return loss_func
  
  
  def loss_visualize(self):
    
    """ Plot loss function against iteration
    """

    plt.figure()
    plt.plot(range(len(Softmax.loss_log)), Softmax.loss_log)
    
    plt.title('Value of loss function for each iteration')
    plt.xlabel('Iteration')
    plt.ylabel('Loss')
    
    plt.show()
    
    
  def predict(self, new_point):
    
    """ Make prediction for new data point of shape (1, m)
        The prediction is a 2-tuple: (class, probability)
    """
    
    new_point = np.concatenate(([0],new_point))
    prediction = np.argmax(self.forward(new_point))
    
    return prediction, self.forward(new_point)[prediction][0]
