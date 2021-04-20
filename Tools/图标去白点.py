from PIL import Image
import os

path = []

for files in os.listdir('./'):
    path.append(files)

for i in path:
    if '.png' in i or '.jpg' in i:
        img = Image.open(i)
        if img.size == (28, 28):
            temp = img.convert("RGBA")
            pim = temp.load()
            pim[0, 0] = (255, 255, 255, 0)
            pim[27, 0] = (255, 255, 255, 0)
            pim[0, 27] = (255, 255, 255, 0)
            pim[27, 27] = (255, 255, 255, 0)
            temp.save(i.replace('.jpg', '.png'))
