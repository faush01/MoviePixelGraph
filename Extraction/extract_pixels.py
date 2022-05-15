from PIL import Image
import os

rootPath = "images"

fileNames = []
for file in os.listdir(rootPath):
    if(file.endswith(".bmp")):
        fileNames.append(os.path.join(rootPath, file))
        
fileNames.sort()
fileCount = len(fileNames)
print ("Number of files : " + str(fileCount))

with open("pixels.tsv", "w") as tsv_file:

	# write the red green blue pixel data to a tsv file
	count = 0
	for file in fileNames:
		img = Image.open(file)
		pixel = img.getpixel((0,0))
		tsv_file.write(str(pixel[0]) + "\t" + str(pixel[1]) + "\t" + str(pixel[2]) + "\n")
		if count % 1000 == 0:
			print (str(count) + " of " + str(fileCount) + " " + str(int(((float(count) / float(fileCount)) * 100))) + "%")
		count += 1
    







