import pandas as pd
import numpy as np
import platform
import csv



def save_to_CSV(images, hashtag):

    path = 'images/{}.csv'.format(hashtag)

    if platform.system() == 'Windows':
        newline = ''
    else:
        newline = None

    with open(path, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        for image in images:
            np_image = np.array(image)
            flat_image = np_image.flatten()
            output_writer.writerow(flat_image)


def read_from_CSV(hashtag):

    path = 'images/{}.csv'.format(hashtag)

    df = pd.read_csv(path, header=None)

    # convert dataframe to numpy array
    images = df.to_numpy()

    # reshape intp 96 x 93 x number of images / len of dataframe
    images = images.reshape(len(images), 96, 96, 3)

    return images
