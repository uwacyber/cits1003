from PIL import Image

# Parameters
filepath = "2424.dmp"
offset = 5233385
width = 1640
height = 350     
bpp = 3  

with open(filepath, 'rb') as f:
    file_data = f.read()

bytes_required = width * height * bpp
chunk = file_data[offset:offset + bytes_required]
img = Image.frombytes('RGB', (width, height), chunk)
img = img.transpose(Image.FLIP_LEFT_RIGHT).rotate(180)
img.save("2424.png")
