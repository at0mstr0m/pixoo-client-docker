from pixoo import Pixoo
import os
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from flask_jwt_extended import JWTManager, create_access_token, get_jwt, get_jwt_identity, unset_jwt_cookies, jwt_required
from datetime import timedelta, datetime, timezone
import json

TWO_DIGIT_NUMBER = re.compile('^[0-9]{1,2}$')
font = ImageFont.truetype('assets/fonts/MP16OSF.ttf', 16)
# font = ImageFont.load_default()

MAC_ADDRESS = os.getenv("MAC_ADDRESS")
PORT = int(os.getenv("PORT", 1337))
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY ", 'super secret default key')

print("Trying to connect to Divoom Timebox-Evo...")
if MAC_ADDRESS:
    pixoo_client = Pixoo(MAC_ADDRESS)
    pixoo_client.connect()
    print("Connection established!")
    pixoo_client.draw_pic(filepath="assets/tomato.png")
else:
    print("Not connected, MAC_ADDRESS is None!")

app = Flask(__name__)
CORS(app)
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
jwt = JWTManager(app)

@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(hours=3))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token 
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # In case there is not a valid JWT. Just return the original respone
        return response

@app.route('/token', methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return {"msg": "Wrong username or password"}, 401
    access_token = create_access_token(identity=username)
    response = {"access_token":access_token}
    return response

@app.route('/profile')
@jwt_required()
def my_profile():
    response_body = {
        "name": "Max Mustermann",
        "about" :"Hallo! Hier könnte Ihre Werbung stehen!"
    }
    return jsonify(response_body)

@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

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
    response = {
        "result": "success",
        "num": num,
    }
    return jsonify(response), 200


@app.route('/ticker', methods=['POST'])
def ticker():
    text = request.json.get("text", '')
    text_width, text_height = font.getbbox(text)[2:]
    canvas = Image.new('RGB', (text_width, text_height))
    draw = ImageDraw.Draw(canvas)
    draw.text((0, 0), text, 'white', font)
    # canvas.save('test.png', 'PNG')
    frames = []
    upper = 3
    lower = upper + 16
    for i in range(canvas.width + 16):
        frames.append(canvas.crop((i - 16, upper, i, lower)))
    byte_stream = BytesIO()
    frames[0].save(byte_stream,
                   format='GIF',
                   append_images=frames,
                   save_all=True,
                   duration=75,
                   loop=0)
    byte_stream.seek(0)
    animation = Image.open(byte_stream)
    frames = pixoo_client.gif_to_frames(animation, 1)
    pixoo_client.send_animation(frames)
    return jsonify({'text': text}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
