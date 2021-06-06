from PIL import Image


def convert_image_to_ascii(path, width, chars=None):
    if chars is None:
        chars = [' ', '.', ',', '~', '?', '%', '@']

    num_chars = len(chars)
    final_ascii = ''

    with Image.open(path).convert('L') as image:
        height = int(width * (image.height / image.width)) // 2
        image = image.resize((width, height))

        index = 0

        for pixel in image.getdata():

            final_ascii += chars[min(
                int(pixel * num_chars / 255),
                num_chars - 1
            )]

            index += 1
            if index >= width:
                index = 0
                final_ascii += '\n'

    return final_ascii
