# USAGE
# python search.py --index index.csv --query queries/103100.png --result-path dataset

# import the necessary packages
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher
import argparse
import cv2
import os
import glob
from skimage import io	
from skimage.color import rgb2gray
import numpy as np
from matplotlib import pyplot as plt

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))

# load the query video and describe it
temp = "/home/ankita/btp7/final/temp"
i=0
# print path_video
cap = cv2.VideoCapture(args["query"])
if cap.isOpened():
	rval , frame = cap.read()
else:
	rval = False
print rval
print args["query"]
while rval:
	
	rval, frame = cap.read()
	if not rval : break
	name = str(i) +'.png'
	cv2.imwrite(os.path.join(temp ,name ), frame)
	i=i+1
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
avg_int = []
no_frames = i
print no_frames

for img in glob.glob(temp+'/*png'):
	
	image = io.imread(img)
	
	im= rgb2gray(image)
	avg_int.append(np.mean(im))
	

	# print(np.mean(im))   

# for i in avg_int:
#     print i

diff = [avg_int[p+1]-avg_int[p] for p in range(len(avg_int)-1)]

# y = diff
# plt.plot(y)
# plt.show()
print diff.index(min(diff))
name1 = temp+'/'+ str(diff.index(min(diff))) +'.png'

print diff.index(max(diff))
name2 = temp+'/'+ str(diff.index(max(diff))) +'.png'

# image1 = cv2.imread(name1)
# save_name = fold +"#"+ video.split('.')[0]+'_1.png'
# cv2.imwrite(os.path.join(data ,save_name ), image1)
# image2 = cv2.imread(name2)
# save_name = fold +"#"+ video.split('.')[0]+'_2.png'
# cv2.imwrite(os.path.join(data ,save_name ), image2)


query = cv2.imread(name2)

for the_file in os.listdir(temp):
	file_path = os.path.join(temp, the_file)
	try:
		if os.path.isfile(file_path):
			os.unlink(file_path)
		#elif os.path.isdir(file_path): shutil.rmtree(file_path)
	except Exception as e:
		print(e)
































# query = cv2.imread(args["query"])
features = cd.describe(query)

# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)

result_images = []
# display the query
cv2.imshow("Query", query)

# loop over the results
path_video = []
for (score, resultID) in results:
	# load the result image and display it
	result = cv2.imread(args["result_path"] + "/" + resultID)
	result_images.append(result)
	fold = resultID.split('#')[0]
	x = resultID.split('#')[1]

	name = x.rsplit('_',1)[0]
	print fold
	
	
	
	
	arr = os.listdir('data/'+fold)
	ext = arr[0].split('.')[1]

	video = 'data/'+fold+'/'+name+'.'+ext
	path_video.append(video)
	
	print video
	# cv2.imshow("Result", result)
	# cv2.waitKey(0)


plt.subplot(4,4,2),plt.imshow(query)
plt.title('Query'), plt.xticks([]), plt.yticks([])

plt.subplot(4,4,5),plt.imshow(result_images[0])
plt.title('Result 1'), plt.xticks([]), plt.yticks([])

plt.subplot(4,4,6),plt.imshow(result_images[1])
plt.title('Result 2'), plt.xticks([]), plt.yticks([])

plt.subplot(4,4,7),plt.imshow(result_images[2])
plt.title('Result 3'), plt.xticks([]), plt.yticks([])

plt.subplot(4,4,8),plt.imshow(result_images[3])
plt.title('Result 4'), plt.xticks([]), plt.yticks([])

plt.subplot(4,4,9),plt.imshow(result_images[4])
plt.title('Result 5'), plt.xticks([]), plt.yticks([])

plt.subplot(4,4,10),plt.imshow(result_images[5])
plt.title('Result 6'), plt.xticks([]), plt.yticks([])

plt.subplot(4,4,11),plt.imshow(result_images[6])
plt.title('Result 7'), plt.xticks([]), plt.yticks([])

plt.subplot(4,4,12),plt.imshow(result_images[7])
plt.title('Result 8'), plt.xticks([]), plt.yticks([])

plt.subplot(4,4,13),plt.imshow(result_images[8])
plt.title('Result 9'), plt.xticks([]), plt.yticks([])

plt.subplot(4,4,14),plt.imshow(result_images[9])
plt.title('Result 10'), plt.xticks([]), plt.yticks([])

plt.subplot(4,4,15),plt.imshow(result_images[10])
plt.title('Result 11'), plt.xticks([]), plt.yticks([])

plt.subplot(4,4,16),plt.imshow(result_images[11])
plt.title('Result 12'), plt.xticks([]), plt.yticks([])
plt.show()
