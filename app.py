import qrcode

data = 'https://time.com/'
img = qrcode.make(data)
img.save('qrcode.png')
