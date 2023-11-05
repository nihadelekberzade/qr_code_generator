import qrcode
import random
import string
import os
from PIL import Image
data = input('Enter you link : ')
img = qrcode.make(data)


# Define the characters you want to use in the random string
characters = string.ascii_letters + string.digits  # letters and digits

# Generate a random 5-character string
image_name = ''.join(random.choice(characters) for _ in range(5))


# Specify the folder name you want to create
folder_name = "qrcodes"
if not os.path.exists(folder_name):
    # Use os.makedirs() to create the folder
    os.makedirs(folder_name)

img.save(f'{folder_name}/{image_name}.png')

print(f'Your file is located in {folder_name}/{image_name}.png')

image = Image.open(f"{folder_name}/{image_name}.png")  # Replace "your_image.jpg" with the path to your image file

# Show the image using the default image viewer
image.show()

