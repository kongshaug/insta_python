from insta_bot import instagram_bot
from neural_network import neural_network

# cat_bot = instagram_bot("cat")
# dog_bot = instagram_bot("dog")
# tree_bot = instagram_bot("tree")


# cat_bot.get_images(1500)
# dog_bot.get_images(1500)
# tree_bot.get_images(1500)

network = neural_network(["cat", "car", "pizza"])
network.make_model()
network.train_network()
# network.test_network()

network.pickle_network()
network.get_pickled_network()

network.predict(
    "https://www.ecosia.org/images?q=bil#id=D33193781FF18D45B9AC73F4EC054E43E37310F7"
)

