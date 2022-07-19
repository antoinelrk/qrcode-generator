# Script by @antoinelrk (08/06/2022)
import qrcode
import os

os.mkdir("./storage")
data = input('Action, url, text: ')
filename = input('filename (without .jpg): ')
img = qrcode.make(data)
img.save('storage/' + filename + '.jpg')
print('Saved as ' + filename + '.jpg')