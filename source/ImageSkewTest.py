import sys
from PIL import Image

img = Image.open('BlackOutCrop.png')
width, height = img.size
m = -0.259
xshift = abs(m) * width
new_width = width + int(round(xshift))
img = img.transform((new_width, height), Image.AFFINE,
        (1, m, -xshift if m > 0 else 0, 0, 1, 0), Image.BICUBIC)
img.save('BlackOutSkewTest.png')

img.crop((70, 22, 2104, 274)).save('FinalSkewCropTest.png')