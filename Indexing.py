from Histogram import RGBHistogram
import argparse
import cPickle
import glob
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
    help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
    help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())

#key = filename, value = computedfeatures
index = {}

#now we initialize the Histogram
desc = RGBHistogram([8,8,8])

for imagePath in glob.glob(args["dataset"]+"/*.png"):
	#extract the image id
	k = imagePath[imagePath.rfind("/")+1:]
	print k

	image = cv2.imread( imagePath )
	features = desc.describe( image )
	index[k] = features

with open(args["index"], "w") as file:
	file.write(cPickle.dumps(index))

