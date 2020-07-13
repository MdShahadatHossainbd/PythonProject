import PIL
from PIL import Image

mywidth = 5000
myhight = 3332

img = Image.open('shahadat10.jpg')
img = img.resize((mywidth,myhight),PIL.Image.ANTIALIAS)
img.save('resize.jpg')