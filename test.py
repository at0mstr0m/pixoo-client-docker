from pixoo import Pixoo
import os

pixoo_client = Pixoo(os.getenv("MAC_ADDRESS"))
print("Trying to connect...")
pixoo_client.connect()
print("Connection established!")

pixoo_client.draw_pic("pokeball.png")