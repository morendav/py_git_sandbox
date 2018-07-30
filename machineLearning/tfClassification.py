#######################################
# Tensor Flow Classificaion
# Date: July 2018
#
#   Walkthrough from online reference material: how to use tensor flow towards applied machine learning for a simple classificaiton algorithm
#   https://www.tensorflow.org/tutorials/keras/basic_classification
#######################################

#######################################
###     CodeBlock: InitVar, Import
#######################################
#   TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

#   Helper libraries
import numpy as np
import matplotlib.pyplot as plt

#   import sample data of clothing for classificaiton
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#   DebugPoint: Explore datasets
# train_images.shape
# len(train_labels)
# test_images.shape
# len(test_labels)
# plt.figure()
# plt.imshow(train_images[0])
# plt.colorbar()
# plt.gca().grid(False)
# plt.show()

#   Standardized hte test_images
train_images_std = train_images / 255.0
test_images_std = test_images / 255.0
