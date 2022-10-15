import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.applications import ResNet50
from matplotlib import pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.preprocessing.image import ImageDataGenerator

train_images = os.listdir('C:/repos/geoanswr/generator/src')
train_metadata = pd.read_csv('C:/repos/geoanswr/generator/results.csv')

def dataset_display(sample, title):
    img = load_img(f'C:/repos/geoanswr/generator/src/{train_images[sample]}', target_size=(252, 252))
    imgplot = plt.imshow(img)
    plt.title(title)
    plt.show()

dataset_display(3, 'image')

X_train = train_metadata.drop(['latitude', 'longitude'], axis=1)
y_train = train_metadata.drop('file_name', axis=1)