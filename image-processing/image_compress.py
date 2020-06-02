from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
#new_img = img.resize((400, 400))
# auto-adjust to normal aspect ratio
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
print(img.size)
