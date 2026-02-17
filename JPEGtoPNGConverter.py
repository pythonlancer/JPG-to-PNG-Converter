#Include all required modules
import sys
import os
from PIL import Image

#Let's grab the first and second arguments from the terminal command we -
#use to run this file
jpg_image_folder = sys.argv[1]
png_image_folder = sys.argv[2]

#Now, let's check if the PNG folder exists and if not, we create it
if not os.path.exists(png_image_folder):
    os.mkdir(png_image_folder)

#Loop through the jpeg_folder, convert all Jpegs to png and finally save them to the png_folder.
for image_filename in os.listdir(jpg_image_folder):
    img = Image.open(f'{jpg_image_folder}{image_filename}')
    remove_jpg_extension = os.path.splitext(image_filename)[0]
    img.save(f'{png_image_folder}/{remove_jpg_extension}.png','png')
    print("Image saved")
print("Done! All Images have been converted and added to the png_folder")
