from ij import IJ
from ij.io import FileSaver
from os import path

imp = IJ.getImage()
fs = FileSaver(imp)
#print imp
#ImagePlus, ImageSatck, CompositeImage

folder = "/home/severine/Documents/processed_images"

if path.exists(folder) and path.isdir(folder):
	print "folder exists:", folder
	filepath = path.join(folder, "test.tif")
	if path.exists(filepath):
		print "file exists"
	elif fs.saveAsTiff(filepath):
		print "saved", filepath
else:
	print "folder does not exist"