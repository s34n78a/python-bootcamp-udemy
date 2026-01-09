from PIL import Image
import os

import PIL

# Open an image file
def open_image(file_name):
    image_path = os.path.join(os.getcwd(), "img_editing", file_name)
    try:
        img = Image.open(image_path)
        return img
    except IOError:
        print("Unable to open image file.")
        return None
    
# convert to jpg
def convert_to_jpg(image, new_name):
    new_name += '.jpg'
    rgb_image = image.convert('RGB')
    rgb_image.save(new_name)
    return open_image(new_name)

file_name = 'example.jpg'
mac = open_image(file_name)
if mac:
    print(mac.format, mac.size, mac.mode)

pencil = open_image('pencils.jpg')
if pencil:
    print(pencil.format, pencil.size, pencil.mode)
    pencil.crop((0, 0, 100, 100))  # Crop and show a portion of the image
    pencil.rotate(45)  # Rotate and show the image
    pencil.resize((200, 200))  # Resize and show the image
    pencil.convert("L")  # Convert to grayscale and show the image
    pencil.save(os.path.join(os.getcwd(), "img_editing", "pencils_gray.jpg"))

red = open_image('red_color.jpg')
blue = open_image('blue_color.png')
if red and blue:
    red.putalpha(128)  # Set transparency for red image
    #convert png to jpeg
    blue = convert_to_jpg(blue, os.path.join(os.getcwd(), "img_editing", "blue_color_converted"))

    blue.putalpha(128)  # Set transparency for blue image

    blue.paste(red, (0, 0), red)  # Overlay red on blue
    blue.save(os.path.join(os.getcwd(), "img_editing", "combined_image.png"))