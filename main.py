from PIL import Image, ImageFilter
from math import sqrt
#Read image
im = Image.open('doge.jpg')
red = 0
green = 1
blue = 2


def swapRGB(im):
	newimdata = []
	for pixel in im.getdata():
		#swap red>green, green>blue and blue>red:
		newpixel = (pixel[green], pixel[blue], pixel[red])
		#if pixel[blue] > 200: # and pixel[red] + pixel[green] < 200:
		#    newpixel = [0,0,0]
		newimdata.append(tuple(newpixel))
	newim = Image.new(im.mode, im.size)
	newim.putdata(newimdata)
	return newim


def redden(im):
	newimdata = []
	for pixel in im.getdata():
		#lower blue and green, raise red:
		newpixel = list(pixel)
		newpixel[red] = int(pixel[red] * 1.5)
		newpixel[green] = int(pixel[green] * 0.75)
		newpixel[blue] = int(pixel[blue] * 0.75)
		newimdata.append(tuple(newpixel))
	newim = Image.new(im.mode, im.size)
	newim.putdata(newimdata)
	return newim


def burncorner(im):
	newimdata = []
	width, height = im.size
	for row in range(height):
		for col in range(width):
			pixel = im.getpixel((col, row))
			#calculate a burn value based on how far away from the corner we are
			burnval = (height - row + width - col) / 500
			#multiply each rgb value by the same burn value
			newpixel = [int(x * burnval) for x in list(pixel)]
			newimdata.append(tuple(newpixel))
	newim = Image.new(im.mode, im.size)
	newim.putdata(newimdata)
	return newim


def vignette(im):
	newimdata = []
	width, height = im.size
	vmid = width // 2
	hmid = height // 2
	radius = min(vmid, hmid)
	for row in range(height):
		for col in range(width):
			pixel = im.getpixel((col, row))
			# calculate crow flies distance from midpoint using pythagoras
			dist = sqrt((hmid - row)**2 + (vmid - col)**2)
			# calculate a brightness weight based on this distance
			weight = (radius - dist + 20) / 120
			#multiply each rgb value by the same burn value
			newpixel = [min(x, int(x * weight)) for x in list(pixel)]
			newimdata.append(tuple(newpixel))
	newim = Image.new(im.mode, im.size)
	newim.putdata(newimdata)
	return newim

#PIL ImageFilter built in standard filter example
def standard(im):
	newimdata = []	
	newim = im.filter(ImageFilter.BLUR)
	newim.putdata(newimdata)
	return newim
'''
standard filters are
  BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE
  EMBOSS, FIND_EDGES, SHARPEN, SMOOTH, SMOOTH_MORE
  see https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html
'''


# kernel-based filter code
def kernelfilter(im,kernel):
	newimdata = []	
	newim = im.filter(ImageFilter.Kernel(ksize,kernel,1,0))
	newim.putdata(newimdata)
	return newim
# see https://setosa.io/ev/image-kernels/ for further examples
edge =   [ -1, -1, -1 ,
           -1,  9, -1 ,
           -1, -1, -1  ]
emboss = [ -2, -1,  0 ,
           -1,  1,  1 ,
            0,  1,  2  ]
blur =   [ 0.125, 0.125, 0.125 ,
           0.125, 0.25, 0.125 ,
           0.125, 0.125, 0.125  ] 
identity=[ 0, 0, 0 ,
           0, 1, 0 ,
           0, 0, 0  ]
ksize = (3,3)
'''
newimage = swapRGB(im)
newimage.save('dogeSwapped.jpg', "JPEG")
print("done swap")
newimage = redden(im)
newimage.save('dogeRed.jpg', "JPEG")
print("done red")
newimage = burncorner(im)
newimage.save('dogeBurn.jpg', "JPEG")
print("done burn")
newimage = vignette(im)
newimage.save('dogeVignette.jpg', "JPEG")
print("done vignette")
'''
newimage = standard(im)
newimage.save('dogeStandard.jpg', "JPEG")
print("done standard")
newimage = kernelfilter(im,emboss)
newimage.save('dogeEmboss.jpg', "JPEG")
print("done emboss")
