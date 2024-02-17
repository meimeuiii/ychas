from PIL import Image
from PIL import ImageFilter
import os
file_list = os.listdir("photos/")
for photo_name in file_list:
    photo = Image.open("photos/"+photo_name)
    photo = photo.filter(ImageFilter.EMBOSS)
    photo.save("edited_photo/"+photo_name)
    photo.close()

print(file_list)


