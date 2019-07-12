from PIL import Image

def Image_ScannerTeam2(imageNum):
    image = Image.open('LobbySlotSC' + str(imageNum) + '.png')
    width, height = image.size
    rgb_image = image.convert('RGB')

    bronze_xTracker = []

    for y in range(0, height):
        for x in range(0, width):
            r, g, b = rgb_image.getpixel((x, y))

            if r > 160 and r < 180 and g > 90 and g < 110 and b > 60 and b < 80:
                bronze_xTracker.append(x)
                print("HAI")

    print(bronze_xTracker)
    image.crop((0, 0, min(bronze_xTracker), height)).save('LobbySlotSC' + str(imageNum) + '.png')

Image_ScannerTeam2(7)