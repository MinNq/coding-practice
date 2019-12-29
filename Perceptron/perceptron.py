import numpy as np
import matplotlib.pyplot as plt


class perceptron:
  
  def __init__(self, ndim):
    
    self.ndim = ndim
    
    # Weight vetor initialization
    self.weight = np.random.randn(self.ndim + 1, 1)
  
  
  def train(self, data):
    
    """ Perceptron learning algorithm:
          Weight initialization (already done in __init__)
          While not converged:
            1. Shuffle observations
            2. Update weight with each misclassified data point if any
            3. Repeat
    """
    
    terminate = False
    
    while not terminate:
      
      np.random.shuffle(data)
      print(self.weight)
      still_misclassify = False
      
      for data_point in data:
        if self.misclassify(data_point):
          self.update(data_point)
          still_misclassify = True
          
      if not still_misclassify:
        terminate = True
        
    print('Training completed!')
        
        
  """ Data is of shape (n, m + 1),
      in each row:
        first entry is label (-1 or 1)
        the rest is data point of shape (1, m)
  """
  
  def inp(self, data_point):
    
    """ Create augmented data point of shape (m, 1)
    """
    
    point = np.concatenate((data_point, [1]))

    return point[1:].reshape((self.ndim + 1, 1))
  
  
  def label(self, data_point):
    
    return data_point[0]
    
    
  def misclassify(self, data_point):
  
    """ See if model agrees with label
    """
  
    sign = np.sign(np.dot(self.weight.T, self.inp(data_point)))
  
    return not sign == self.label(data_point)


  def update(self, data_point):
    
    self.weight += self.label(data_point)*self.inp(data_point)
        
        
  def predict(self, new_point):
    
    """ Make prediction for new data point of shape (1, m)
    """
    
    new_point = np.concatenate(([0], new_point))
    sign = np.sign(np.dot(self.weight.T, self.inp(new_point)))
    
    return sign if sign == 1 else -1
