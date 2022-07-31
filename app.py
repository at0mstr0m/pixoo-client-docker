from pixoo import Pixoo
import os
import re
from flask import Flask, request
from PIL import Image

TWO_DIGIT_NUMBER = re.compile('^[0-9]{1,2}$')

MAC_ADDRESS = os.getenv("MAC_ADDRESS")
PORT = int(os.getenv("PORT"))

pixoo_client = Pixoo(MAC_ADDRESS)
print("Trying to connect...")
pixoo_client.connect()
print("Connection established!")
pixoo_client.draw_pic(filepath="assets/tomato.png")

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, Docker!', 200


@app.route('/draw_pic', methods=['GET'])
def draw_pic():
    pixoo_client.draw_pic(filepath="pokeball.png")
    return 'draw_pic', 200


@app.route('/draw_gif', methods=['GET'])
def draw_gif():
    # set speed to 1 to preserve the gif's original speed
    pixoo_client.draw_gif("pong.gif", 1)
    return 'draw_gif', 200


@app.route('/draw_number', methods=['GET'])
def draw_number():
    num = request.args.get('num', '0')
    if not re.match(TWO_DIGIT_NUMBER, num):
        return 'only 1 or 2 digit numbers are accepted', 400
    # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.alpha_composite
    # final_image = Image.new("RGBA", (16, 16))
    final_image = Image.open("assets/tomato.png")
    if len(num) == 1:
        num_asset = Image.open(f'assets/{int(num)}_middle.png')
        final_image.alpha_composite(num_asset)
    elif len(num) == 2:
        left_num_asset = Image.open(f'assets/{int(num[0])}_left.png')
        right_num_asset = Image.open(f'assets/{int(num[1])}_right.png')
        final_image.alpha_composite(left_num_asset)
        final_image.alpha_composite(right_num_asset)
    pixoo_client.draw_pic(image=final_image)
    return 'draw_pic', 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
