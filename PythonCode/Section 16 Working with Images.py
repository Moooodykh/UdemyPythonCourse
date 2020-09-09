# ------------------------ Section 16: Section 16 Working with Images is from part 125 to 128   -----------------------------

path =r'E:\PROGRAMMING\github\UdemyPythonCourse\PythonCode\PDFs_Sheets\Exercise_Files'
""" # PIL : python Image Library is the main library
# We will work with PILLOW lib, Pip install pillow

import os
from PIL import Image
### EVER THING WITH IMAGE IS TUPLES
image_dir = os.getcwd() + '\\Images'
os.chdir(image_dir)

mac = Image.open('example.jpg')

print(type(mac))
# mac.show()# showing the image
print(mac.size)
print(mac.filename)
print(mac.format_description)
# mac.crop((0,0,100,100)).show() # x,y,w,h  ALL are coordinate

start_x = 1993 / 2
start_y = 1257 / 3

# mac.crop((start_x-200,start_y,start_x +200,1257)).show() # CUT THE MAC OBJECT

pencils = Image.open('pencils.jpg')
# pencils.show()
print(pencils.size)

# pencils.crop((0,0,700,400)).show()

# Start is at top corner
x = 0
y = 0

#grab about 10% in Y direction and 30% of X direction
w = 1950 / 3
h = 1300 / 10

# pencils.crop((x,y,w,h)).show()

# Let's try from bottom

x = 0
y = 1100
w = 1950 / 3
h = 1300
# pencils.crop((x,y,w,h)).show()

### Copying and Pasting Images
image_copy = mac.crop((start_x-200,start_y,start_x +200,1257))
mac.paste(im=image_copy,box=(0,0))  #copy and paste the new image(image_copy) on the top of mac picture
# in the position (0,0)
mac.paste(im=image_copy,box=(796,0))  #copy and paste the new image(image_copy) on the top of mac picture
# mac.show()

w,h = mac.size
new_w =int(w/3)
new_h =int(h/3)

# mac.resize((new_w,new_h)).show() 
#NOTE THAT THIS IS NOT A PERMANENT CHANGE
# IF YOU WANT TO HAVE A PERMANET SOLUTION
# mac = mac.rezise((new_w,new_h))

#Can also stretch and squeeze
# mac.resize((3000,500)).show()

### ROTATING
# pencils.rotate(90).show()
# pencils.rotate(120).show()
# pencils.rotate(90,expand=True).show()
# pencils.rotate(120,expand=True).show()

####Transparency
# We can add an alpha value (RGBA stands for RED,Green,Blue, Alpha) where values can go from 0 to 255. If Alpha is 0 the image is completely transparent, if it is 255 then its completely opaque.
# You can create your own color here to check for possible values: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool
# We can adjust image alpha values with the putalpha() method:


# Transparency and masking can be much more complex than what we've shown here,
# if you find yourself needing something more, check out the documentation:
# https://pillow.readthedocs.io/en/stable/

red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')
# r_255 = red.putalpha(255) #RED
# r_255.show()
# r_0 = red.putalpha(0) # TRANSPARENT
# r_0.show()
# r_128 =red.putalpha(128) # IN BETWEEN
# r_128.show()
# blue.show()

# blue.paste(red,box=(0,0),mask=red)
# blue.paste(im=red,box=(0,0),mode=red).show()
#
blue.show()
"""
# # # # # # # # # #  part 125 ( Advanced Numbers) # # # # # # # # #
# # # # # # # # # #  part 126 ( Advanced Sets) # # # # # # # # #
# # # # # # # # # #  part 127 ( Advanced Dictionaries) # # # # # # # # #
# # # # # # # # # #  part 128 ( Advanced Lists) # # # # # # # # #
