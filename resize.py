import sys
import os
from PIL import Image

full_path = str(sys.argv[1])
file_path = os.path.dirname(full_path)
filename = os.path.basename(full_path)
file = os.path.splitext(filename)
img_name = file[0]
file_ext = file[1]

new_filename = (file_path + '/' + img_name + '_thumb' + file_ext)

image = Image.open(full_path)
image.thumbnail((400, 400))
image.save(new_filename)
print(image.size)