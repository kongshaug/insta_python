import csv_connection
import matplotlib.pyplot as plt
import numpy as np
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras import models
from keras import layers
import pickle
from skimage import io
from skimage.transform import resize


class neural_network:
    def __init__(self, hashtags):
        self.hashtags = hashtags  # [cat, dog, tree]
        self.images = []
        self.targets = []
        self.target_translator = {}

        self.get_images_from_csv()

    def get_images_from_csv(self):

        for idx, hashtag in enumerate(self.hashtags):
            self.target_translator[hashtag] = idx
            images_from_csv = csv_connection.read_from_CSV(hashtag)
            for image in images_from_csv:
                self.images.append(image)
                self.targets.append(idx)

        print("images from csv files are received")
        self.prepare_data()

    def prepare_data(self):
        self.images = np.array(self.images)
        self.targets = np.array(self.targets)

        print("Shape of images {}".format(self.images.shape))
        print("Shape of targets {}".format(self.targets.shape))
        print(self.target_translator)

        X = self.images
        y = to_categorical(self.targets, len(self.hashtags))

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.33)

        print("66% of the data {} and 33% of the data {}".format(
            len(self.X_train), len(self.X_test)))

    def make_model(self):
        model = models.Sequential()
        model.add(layers.Conv2D(
            32, (3, 3), activation='relu', input_shape=(96, 96, 1)))
        # Max Pooling to reduce the spatial dimensions of the output volume. pool_size: integer or tuple of 2 integers, factors by which to downscale (vertical, horizontal)
        model.add(layers.MaxPool2D((2, 2)))
        # does not need input_shape, since it gets it from previous layer
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.MaxPool2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        # rewrite tensor to single vector of values
        model.add(layers.Flatten())
        model.add(layers.Dense(64, activation='relu'))
        # softmax is good for output layer because Softmax outputs probabilities range. The range will 0 to 1, and the sum of all the probabilities will be equal to one. If the softmax function used for multi-classification model it returns the probabilities of each class and the target class will have the high probability.
        model.add(layers.Dense(len(self.hashtags), activation='softmax'))

        model.compile(loss='categorical_crossentropy',  # loss is how to meassure how wrong the model is on its predictions
                      optimizer='adam',  # rmsprop
                      # what do we care about in our model
                      metrics=['accuracy'],
                      )

        self.model = model

    def train_network(self):
        self.model.fit(self.X_train,
                       self.y_train,
                       epochs=10,
                       verbose=True,
                       batch_size=64,
                       validation_split=0.1)  # checking periodically how well we are doing

    def test_network(self):
        results = self.model.evaluate(self.X_test, self.y_test)
        print('test loss, test acc:', results)
    
    def predict(self, image_link):
        image = io.imread(image_link)
        array_image = resize(image, (96, 96, 3))
        image_list = np.array([array_image])
        predicted = self.model.predict(image_list)
        print(predicted)
    
    def pickle_network(self):
        pickle_out = open("network.pickle", "wb")
        pickle.dump(self.model, pickle_out)
        pickle_out.close()
    
    def get_pickled_network(self):
        pickle_in = open("network.pickle", "rb")
        self.model = pickle.load(pickle_in)



