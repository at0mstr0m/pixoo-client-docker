from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

# font = ImageFont.truetype('pixoo-api/assets/fonts/windows_command_prompt.ttf', 16)
font = ImageFont.truetype('pixoo-api/assets/fonts/MP16OSF.ttf', 16)
# font = ImageFont.truetype('pixoo-api/assets/fonts/MP16REG.ttf', 16)
# font = ImageFont.truetype('pixoo-api/assets/fonts/MP16SC.ttf', 16)
# font = ImageFont.truetype('pixoo-api/assets/fonts/MP16TO1.ttf', 16)
# font = ImageFont.truetype('pixoo-api/assets/fonts/RetGanon.ttf', 16)
# font = ImageFont.truetype('pixoo-api/assets/fonts/PrStart.ttf', 16)
# font = ImageFont.truetype('pixoo-api/assets/fonts/prstartk.ttf', 16)

text = "|QÖBj"
# text_width, text_height = font.getsize(text)
text_width, text_height = font.getbbox(text)[2:]
# text_width += 1
print(f'font.getsize() = {font.getsize(text)}')
print(f'font.getbbox() = {font.getbbox(text)[2:]}')
canvas = Image.new('RGB', (text_width, text_height))
draw = ImageDraw.Draw(canvas)
draw.text((0, 0), text, 'white', font)
canvas.save('test.png', 'PNG')
####
frames = []
for i in range(canvas.width + 16):
    frames.append(canvas.crop((i - 16, -1, i, 15)))
output = BytesIO()
frames[0].save("test.gif",
               format='GIF',
               append_images=frames,
               save_all=True,
               duration=100,
               loop=0)
