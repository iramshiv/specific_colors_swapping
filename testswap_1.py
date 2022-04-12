from PIL import Image

__author__ = "Sethuraman Ramanathan"
__version__ = "1.0.0"
__maintainer__ = "Sethuraman Ramanathan"
__email__ = "iramshiv@gmail.com"
__status__ = "r&d"
__image_reference__ = 'https://unsplash.com/photos/QeVmJxZOv3k?utm_source=unsplash&utm_medium=referral&utm_content' \
                      '=creditShareLink '

src_img = Image.open("./images/source.jpg")  # input image

img_width = src_img.size[0]
img_height = src_img.size[1]

for x in range(0, img_width):  # process all pixels

    for y in range(0, img_height):

        data = src_img.getpixel((x, y))

        # logic for target and result colors swap
        if 21 in data:
            src_img.putpixel((x, y), 255)

src_img.save('./images/resulted.jpg')  # result image
