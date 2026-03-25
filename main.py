from PIL import Image

char = "@%#*+=-:."
img_path = input("Image Path / location => ")

img = Image.open(img_path)
img = img.resize((100, 50))
img = img.convert("L")

for Y in range(img.height):
    for x in range(img.width):
        gray = img.getpixel((x, Y))
        print(char[gray * len(char) // 256], ends="")
    print("")
