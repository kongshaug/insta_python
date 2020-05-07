import csv_connection
import matplotlib.pyplot as plt
import numpy as np
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split


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

    def prepare_data(self):
        self.images = np.array(self.images)
        self.targets = np.array(self.targets)

        print("Shape of images {}".format(self.images.shape))
        print("Shape of targets {}".format(self.targets.shape))
        print(self.target_translator)

        X = self.images
        y = to_categorical(self.targets, len(self.hashtags))

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.33
        )

        print(
            "66% of the data {} and 33% of the data {}".format(
                len(self.X_train), len(self.X_test)
            )
        )
