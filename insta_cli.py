import argparse
import pickle
from insta_bot import instagram_bot
from neural_network import neural_network

parser = argparse.ArgumentParser(
    description="This program fetchs images, makes a neural network and is then able to predict images")

parser.add_argument(
    "-n",
    "--number-of-images",
    type=int,
    required=False,
    help="Enter number of images to download",
)

parser.add_argument(
    "-ha",
    "--hashtags",
    nargs="*",
    type=str,
    required=False,
    help="Enter hashtags for the categories in the neural network",
)

parser.add_argument(
    "-t", "--test", action="store_true", required=False, help="Test the neural network"
)

parser.add_argument(
    "-l",
    "--link",
    type=str,
    required=False,
    help="Enter link to the image, you want predicted",
)


def get_data_from_instagram(hashtags, number_of_images):
    for hashtag in hashtags:
        bot = instagram_bot(hashtag)
        bot.get_images(number_of_images)
        print(
            "The images has been downloaded to the file {}.csv in /images".format(hashtag))


def make_neural_network(hashtags):
    print("Please wait ...")
    network = neural_network(hashtags)
    network.make_model()
    network.train_network()
    network.pickle_network()
    print("The neural network is trained, pickled and ready for use")


def test_network():
    pickle_in = open("network.pickle", "rb")
    network = pickle.load(pickle_in)
    pickle_in.close()
    network.test_network()


def predict(link):
    pickle_in = open("network.pickle", "rb")
    network = pickle.load(pickle_in)
    pickle_in.close()
    network.predict(link)


arguments = parser.parse_args()
if arguments.hashtags != None and arguments.number_of_images != None:
    get_data_from_instagram(arguments.hashtags, arguments.number_of_images)
elif arguments.hashtags != None and len(arguments.hashtags) > 1:
    make_neural_network(arguments.hashtags)
elif arguments.link != None:
    predict(arguments.link)
elif arguments.test == True:
    test_network()
