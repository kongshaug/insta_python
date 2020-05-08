from insta_bot import instagram_bot
from neural_network import neural_network

cat_bot = instagram_bot("cat")
dog_bot = instagram_bot("dog")
tree_bot = instagram_bot("tree")

cat_bot.get_images(1500)
dog_bot.get_images(1500)
tree_bot.get_images(1500)


#network = neural_network(["cat", "dog", "tree"])
# network.make_model()
# network.train_network()
# network.test_network()
