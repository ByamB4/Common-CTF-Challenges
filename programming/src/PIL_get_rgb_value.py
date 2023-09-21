from PIL import Image

im = Image.open("starmap.bmp")
pix_val = list(im.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]

flag = ""
for i in pix_val_flat:
    if int(i) > 0:
        flag += chr(int(i))

print(flag)
