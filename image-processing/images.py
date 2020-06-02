from PIL import Image, ImageFilter

img = Image.open('./Pokedex/bulbasaur.jpg')
# sharpen
#filtered_img = img.filter(ImageFilter.SHARPEN)
# grey scale
filtered_img = img.convert('L')
#filtered_img.save("SHARPEN.png", 'png')
crooked = filtered_img.rotate(180)
crooked.save("grey.png", 'png')
# crooked.show()
# must input tuple
resize = filtered_img.resize((100, 100))
resize.save("resize_grey.png", 'png')

box = (100, 100, 200, 200)
region = crooked.crop(box)
region.save("crop_grey.png", 'png')
