#^    save pic into png format
#^    read the picture
#^    apply blur with the name gussian.png
#^    resize 100x100 and save as resize.png
#^    crop image 50x50 and save it as crop.png
#^    write your name on the cropped picture and save it by name_me.png
#^    increase the brightness of the picture by thr factor 5 and name it as bright.jpg
#^    rotate an image by 100 and save as rotate.png
#    folder should have original pic saved as original.jpg

from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont
first_image=Image.open("original.PNG")
first_image.show()

first_image.save("My_Pic.png")
print(first_image.size)
first_image.show()

blur=first_image.filter(ImageFilter.GaussianBlur(radius=10))
blur.show()
blur.save("gussian.png")

resized=first_image.crop ((10,10,100,100))
resized.show()
resized.save("resize.png")

resized=first_image.crop ((4,4,50,50))
resized.show()
resized.save("resize.png")

d1=ImageDraw.Draw(first_image)
d1.text((500,500),"Rachelle Difilippo",fill=(50,150,255))
first_image.show()
first_image.save("nameme.jpg")

enhance=ImageEnhance.Brightness(first_image)
output=enhance.enhance(5)
enhance.show()
output.save("bright.png")

second_image=first_image.rotate(100,expand=2)
second_image.show()
("roatated.jpg")
original=first_image.save("original.jpg")