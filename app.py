from pixoo import Pixoo
import os
from flask import Flask, request

MAC_ADDRESS = os.getenv("MAC_ADDRESS")
PORT = int(os.getenv("PORT"))

pixoo_client = Pixoo(MAC_ADDRESS)
print("Trying to connect...")
pixoo_client.connect()
print("Connection established!")
pixoo_client.draw_pic("pokeball.png")

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, Docker!', 200


@app.route('/draw_pic', methods=['GET'])
def draw_pic():
    pixoo_client.draw_pic("pokeball.png")
    return 'draw_pic', 200


@app.route('/draw_gif', methods=['GET'])
def draw_gif():
    pixoo_client.draw_gif("pong.gif", 1) # set speed to 1 to preserve the gif's original speed
    return 'draw_gif', 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
