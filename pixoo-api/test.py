import re
from flask import Flask, request
from PIL import Image

app = Flask(__name__)
# https://stackoverflow.com/a/18922700/13128152
TWO_DIGIT_NUMBER = re.compile('^[0-9]{1,2}$')


@app.route('/draw_number', methods=['GET'])
def draw_number():
    num = request.args.get('num', '0')
    if not re.match(TWO_DIGIT_NUMBER, num):
        return 'only 1 or 2 digit numbers are accepted', 400
    final_image = Image.new("RGBA", (16, 16))
    if len(num) == 1:
        print(f'assets/{int(num)}_middle.png')
        num_asset = Image.open(f'assets/{int(num)}_middle.png')
        final_image.paste(num_asset)
    elif len(num) == 2:
        print(f'assets/{int(num[0])}_left.png')
        left_num_asset = Image.open(f'assets/{int(num[0])}_left.png')
        print(f'assets/{int(num[1])}_right.png')
        right_num_asset = Image.open(f'assets/{int(num[1])}_right.png')
        final_image.paste(left_num_asset)
        final_image.paste(right_num_asset)
    # pixoo_client.draw_pic(image=final_image)
    return 'draw_pic', 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1337)
