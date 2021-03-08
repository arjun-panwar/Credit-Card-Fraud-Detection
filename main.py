from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('list.csv')
font = ImageFont.truetype('LibreBaskerville-Regular.ttf',100)
for index,j in df.iterrows():
    img = Image.open('certificate.jpg')
    draw = ImageDraw.Draw(img)
    image_width = img.width
    image_height = img.height
    text_width, _ = draw.textsize(j['name'], font=font)


    draw.text(xy=((image_width - text_width) / 2,560),text='{}'.format(j['name']),fill=(0,0,0),font=font)
    img.save('pictures/{}.jpg'.format(j['name']))