#
# P1X Zero IoT 
#

# IMPOTS
#
import time
from time import sleep
import picamera
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# DISPLAY
#
disp = Adafruit_SSD1306.SSD1306_128_64(rst=7, i2c_address=0x3D)
disp.begin()

# CAM
#
camera = picamera.PiCamera()
camera.resolution = (640,480)

# VARS
#
W = 128
H = 64
image = Image.new('1', (W, H))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# INTERFACE
#
draw.rectangle((0,0,W-1,H-1), outline=255, fill=0)
draw.text((4, 2),'P1X Zero IoT v0.1',  font=font, fill=255)
draw.line((2, 18, W-3, 18), fill=255)

draw.text((14, 32),'Boooo!',  font=font, fill=255)


disp.image(image)
disp.display()

while True:
	camera.capture('swap.jpg')
	image = Image.open('swap.jpg').rotate(270)
	image = image.resize((W, H), PIL.Image.NEAREST)
	image = image.convert('1')
	disp.image(image)
	disp.display()
	#sleep(1)
