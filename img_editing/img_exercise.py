from PIL import Image
import os

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

word_matrix = open_image('word_matrix.png')
mask = open_image('mask.png')
if word_matrix and mask:
    #print(word_matrix.size, mask.size)
    mask.putalpha(128)
    mask = mask.resize((1015, 559))
    #print(word_matrix.size, mask.size)
    word_matrix.paste(mask, (0,0), mask)
    word_matrix.save(os.path.join(os.getcwd(), "img_editing", "word_reveal.png"))