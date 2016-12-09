from ij import IJ
from ij.io import FileSaver
from os import path

#imp = IJ.getImage()
#fs = FileSaver(imp)
#print imp
#ImagePlus, ImageSatck, CompositeImage

image = IJ.getImage()

fluor = image.duplicate()
brightfield = image.duplicate()

# Work on fluorescence first: assumes brightfield is the first slice
stack = fluor.getStack()
stack.deleteSlice(1)
fluor.setStack(stack)

IJ.run(fluor, 'Make Composite', '')
IJ.run(fluor, 'Flatten', '')

# Work on brightfield now
stack = brightfield.getStack()
num_slices = stack.getSize()
for i in range(num_slices -1):
	stack.deleteLastSlice()
brightfield.setStack(stack)

fluor.show()
brightfield.show()

#folder = "/home/severine/Documents/processed_images"

#if path.exists(folder) and path.isdir(folder):
#	print "folder exists:", folder
#	filepath = path.join(folder, "test.tif")
#	if path.exists(filepath):
#		print "file exists"
#	elif fs.saveAsTiff(filepath):
#		print "saved", filepath
#else:
#	print "folder does not exist"