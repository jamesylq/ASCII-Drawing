import PIL.Image
import math


def resize(image, new_width=150):
    width, height = image.size
    new_height = round(new_width * height / width)
    return image.resize((new_width, new_height))


def to_greyscale(image):
    return image.convert("L")


def pixel_to_ascii(image):
    ASCII_CHARS = '@&Ø‰ĦŒ§#$OŠS¥%¾BAΔJ(iƚȶ?!※⁕ӿ>±*÷=~+++----;;;;;;:::::::©©©©©©©©ooooooooooo•••••••••••••""""""""""""""""\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'˔˔˔˔˔˔˔˔˔˔˔˔˔ˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,...........................................                                           '
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        print(pixel//(255/len(ASCII_CHARS)))
        ascii_str += ASCII_CHARS[math.floor(pixel//(255/len(ASCII_CHARS))) - 1]
    return ascii_str


image = to_greyscale(resize(PIL.Image.open('download.jpeg')))
ascii_str = pixel_to_ascii(image)
img_width = image.width
ascii_str_len = len(ascii_str)
ascii_img = ""
for i in range(0, ascii_str_len, img_width * 2):
    ascii_img += ascii_str[i:i+img_width] + "\n"
print(ascii_img)
with open('ascii_image.txt', 'w') as file:
    file.write(ascii_img)
