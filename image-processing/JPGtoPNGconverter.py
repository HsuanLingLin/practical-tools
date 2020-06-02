import sys
import os
from PIL import Image

# jpg to png converter
# step1. grab first and second argument
src_folder = sys.argv[1]
dest_folder = sys.argv[2]
print(src_folder, dest_folder)

# step2. check is new/ exists, if not create
print(os.path.exists(dest_folder))
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)
# step3. loopr through pokedex then convert images to png
for filename in os.listdir(src_folder):
    img = Image.open(f'{src_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    print(clean_name)
    # step4. save to the new folder
    img.save(f'{dest_folder}{clean_name}.png', 'png')
print('all done!')
p
