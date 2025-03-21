#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
import matplotlib.pyplot
get_ipython().run_line_magic('matplotlib', 'inline')

training_file = open("mnist_dataset/mnist_train_100.csv", 'r')
training_data = training_file.readlines()
training_file.close()


# In[ ]:


print(training_data[0])


# In[ ]:


all_values = training_data[0].split(',')
image_array = numpy.asfarray(all_values[1 : ]).reshape((28, 28))
matplotlib.pyplot.imshow(image_array, cmap = 'Greys', interpolation = 'None')
matplotlib.pyplot.show()


# In[ ]:


input = (numpy.asfarray(all_values[1 : ]) / 255.0 * 0.99) + 0.01
print(input)


# In[ ]:


import numpy
import scipy.special
import matplotlib.pyplot

get_ipython().run_line_magic('matplotlib', 'inline')

class NeuralNetwork :
    
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate) :
       
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        
        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

        self.lr = learningrate
        
        self.activation_function = lambda x : scipy.special.expit(x)
        
    def training(self, input_list, target_list) :
       
        input = numpy.array(input_list, ndmin = 2).T
        target = numpy.array(target_list, ndmin = 2).T
        
        hidden_input = numpy.dot(self.wih, input)
        hidden_output = self.activation_function(hidden_input)
        
        final_input = numpy.dot(self.who, hidden_output)
        final_output = self.activation_function(final_input)
        
        output_error = target - final_output
        hidden_error = numpy.dot(self.who.T, output_error) 
        
        self.who += self.lr * numpy.dot((output_error * final_output * (1.0 - final_output)), numpy.transpose(hidden_output))
        self.wih += self.lr * numpy.dot((hidden_error * hidden_output * (1.0 - hidden_output)), numpy.transpose(input))
        
    def test(self, input_list) :
        
        input = numpy.array(input_list, ndmin = 2).T
       
        hidden_input = numpy.dot(self.wih, input)
        hidden_output = self.activation_function(hidden_input)
        
        final_input = numpy.dot(self.who, hidden_output)
        final_output = self.activation_function(final_input)
        
        return final_output


# In[ ]:


input_nodes = 784
hidden_nodes = 100
output_nodes = 10
learning_rate = 0.2

n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)


# In[ ]:


training_file = open("mnist_dataset/mnist_train.csv", 'r')
training_data = training_file.readlines()
training_file.close()

epochs = 7

for e in range(epochs) :
    for record in training_data :
        all_values = record.split(',')
        input = (numpy.asfarray(all_values[1 : ]) / 255.0 * 0.99) + 0.01
        target = numpy.zeros(output_nodes) + 0.01
        target[int(all_values[0])] = 0.99
        n.training(input, target)


# In[ ]:


test_file = open("mnist_dataset/mnist_test.csv", 'r')
test_data = test_file.readlines()
test_file.close()

scorecard = []

for record in test_data :
    all_values = record.split(',')
    target_value = int(all_values[0])
    input = (numpy.asfarray(all_values[1 : ]) / 255.0 * 0.99) + 0.01
    output = n.test(input)
    model_output = numpy.argmax(output)
    if (model_output == target_value) :
        scorecard.append(1)
    else :
        scorecard.append(0)

scorecard_array = numpy.asarray(scorecard)
print ("performance =", scorecard_array.sum() / scorecard_array.size)

