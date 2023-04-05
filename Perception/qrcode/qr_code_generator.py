import pyqrcode

qr = pyqrcode.create("Major Project", error='H')
qr.png("qrcode/Major Project.png", scale=8)
