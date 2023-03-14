from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

font = ImageFont.truetype('pixoo-api/assets/fonts/MP16OSF.ttf', 16)

text = "|QÖBj"
text_width, text_height = font.getbbox(text)[2:]
print(text_width, text_height)
canvas = Image.new('RGB', (text_width, text_height))
draw = ImageDraw.Draw(canvas)
draw.text((0, 0), text, 'white', font)
canvas.save('test.png', 'PNG')
####
frames = []
upper = 3
lower = upper + 16
for i in range(canvas.width + 16):
    frames.append(canvas.crop((i - 16, upper, i, lower)))
output = BytesIO()
frames[0].save("test.gif",
               format='GIF',
               append_images=frames,
               save_all=True,
               duration=75,
               loop=0)
