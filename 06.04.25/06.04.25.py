from PIL import Image
img = Image.open("cat.png")
w = img.width
h = img.height
cropped_img = img.crop((0, 0, w/2, h))
cropped_img.save('cat_2.png')
cropped_img2 = img.crop((w/2, 0, w, h))
cropped_img2.save('cat_3.png')
img.close()
cropped_img.close()
cropped_img2.close()