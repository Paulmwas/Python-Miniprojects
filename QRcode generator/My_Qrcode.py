import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create('This is an awesome tutorial!!')
qr.png('qrcode.png',scale='10')


