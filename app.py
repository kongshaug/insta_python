from insta_bot import instagram_bot
from neural_network import neural_network

# cat_bot = instagram_bot("cat")
# car_bot = instagram_bot("car")
# pizza_bot = instagram_bot("pizza")

# cat_bot.get_images(1500)
# car_bot.get_images(1500)
# pizza_bot.get_images(1500)

network = neural_network(["cat", "car", "pizza"])
#network.make_model()
#network.train_network()
#network.test_network()

#network.pickle_network()
network.get_pickled_network()

network.predict(
    "https://img.chewy.com/is/image/catalog/120918_MAIN._AC_SL1500_V1496427995_.jpg"
)
network.predict(
    "https://caterville.files.wordpress.com/2013/10/fe0c8-pizza-cat.jpg"
)


