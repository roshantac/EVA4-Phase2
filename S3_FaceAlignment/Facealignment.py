import dlib
import cv2
import numpy as np
from renderFace import renderFace
import matplotlib.pyplot as plt


% matplotlib inline

import matplotlib

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

def writeLandmarksToFile(landmarks, landmarksFileName):
	with open(landmarksFileName, 'w') as f:
		for p in landmarks.parts():
			f.write("%s %s \n" %(int(p.x),int(p.y)))
		f.close()
# landmark location
PREDICTOR_PATH = MODEL_PATH + "shape_predictor_68_face_landmarks.dat"

##############################################################################
!wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
!bzip2 -dk shape_predictor_68_face_landmarks.dat.bz2
##############################################################################

faceDetector = dlib.get_frontal_face_detector()

# The landmark detector is implemented in the shape_predictor class
landmarkDetector = dlib.shape_predictor(PREDICTOR_PATH)


# Read image
imageFilename = DATA_PATH + "images/family.jpg"
im = cv2.imread(imageFilename)

# landmarks will be stored in results/family_i.txt
landmarksBasename = "results/family"
plt.imshow(im[:,:,::-1])
plt.show()




#############################################################################
#				Detect Faces
############################################################################

faceRects = faceDetector(im, 0)
print("Number of faces detected :", len(faceRects))

# List to store landmarks of all detected faces

landmarksAll = []

# OUTPUT : Number of faces detected 5



########################################################
#                Detect Landmarks for each face
#######################################################

# loop over all detected face rectangles

for i in range(0, len(faceRects)):
	newRect = dlib.rectangle(int(faceRects[i].left()),
		int(faceRects[i].top()),
		int(faceRects[i].right()),
		int(faceRects[i].bottom()))

# for every face rectangle run landmarkDetector

landmarks = landmarkDetector(im, newRect)

if i == 0:
	print("Number of landmarks", len(landmarks.parts()))

#store landmarks for current face

landmarksAll.append(landmarks)

# Next we render the outline of face using detected landmarks

renderFace(im, landmarks)

landmarksFileName = landmarksBasename + "_" + str(i)+ ".txt"
print("Saving landmarks to ", landmarksFileName)
writeLandmarksToFile(Landmarks,landmarksFileName)







outputFilename = "results/familyLandmarks.jpg"
print("saving output image to", outputFilename)

cv2.imwrite(outputFilename, im)

plt.figure(figsize=(15,15))
plt.imshow(im[:,:,::-1])
plt.title("Facial Landmark detector")
plt.show()


############################################################################
#Rendering facial landmarks
############################################################################

img = cv.polylines(img, pts,isClosed, color[,thickness[,lineType[,shift]]])


import cv2 
import numpy as np

def drawPolyline(im,landmarks, start, end, isClosed =False):
	points = []
	for i in range(start, end+1):
		points = [landmarks.part(i).x, landmarks.part(i).y]
		points.append(point)
	points = np.array(points, dtype=np.int32)
	cv2.polylines(im,[points],isClosed,(255,200,0), thickness =2, lineType = cv2.LINE_8)


def renderFace(im, landmarks):
	assert(landmarks.num_parts == 68)
	drawPolyline(im, landmarks, 0,16)
	drawPolyline(im, landmarks, 17,21)
	drawPolyline(im, landmarks, 22,26)
	drawPolyline(im, landmarks, 27,30)
	drawPolyline(im, landmarks, 30,35, True)
	drawPolyline(im, landmarks, 36,41, True)
	drawPolyline(im, landmarks, 42,47, True)
	drawPolyline(im, landmarks, 48,59, True)
	drawPolyline(im, landmarks, 60,67, True)


def renderFace2(im, landmarks, color = (0,255,0),radius =3):
	for p in landmarks.parts():
		cv2.circle(im,(p.x,p.y), radius, color, -1)

def writeLandmarksToFile(landmarks, landmarksFileName):
	with open(landmarksFileName, 'w') as f:
		for p in landmarks.parts():
			f.write("%s %s\n", %(int(p.x),int(p.y)))
	f.close()
	



!wget http://dlib.net/files/shape_predictor_5_face_landmarks.data.bz2
!bzip2 -dk shape_predictor_5_face_landmarks.dat.bz2




import dlib
import cv2
import numpy as np 
import faceBlendCommon as fbc
from dataPath import DATA_PATH
from dataPath import MODEL_PATH
import matplotlib.pyplot as plt
%matplotlib inline

import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

PREDICTOR_PATH = MODEL_PATH + "shape_predictor_5_face_landmarks.dat"

faceDetector = dlib.get_frontal_face_detector()
faceDetector = dlib.shape_predictor(PREDICTOR_PATH)

im = cv2.imread(DATA_PATH + "image/face2.png")


plt.imshow(im[:,:,::-1])
plt.title("Image")
plt.show()


points = fbc.getLandmarks(faceDetector, landmarkDetector, im)

points = np.array(points)

im = np.float32(im)/255.0


h = 600
w = 600

inNorm, points = fbc.normalizeImageAndLandmarks((h,w),im,points)

imNorm = np.uint8(imNorm*255)


#Display the results

plt.imshow(imNorm[:,:,::-1])
plt.title("Aligned Image")
plt.show()




##############################################################################
##						Image Alignment code
##############################################################################





def normalizeImagesAndLandmarks(outSize, imIn, pointsIn):
	h,w = outSize

	if len(pointsIn) == 68:
		eyecornerSrc =[pointsIn[36], pointsIn[45]]
	elif len(pointsIn) == 5:
		eyecornerSrc = [pointsIn[2], pointsIn[0]]

	eyecornerDst = [(np.int(0.3*w), np.int(h/3)), (np.int(0.7*w), np.int(h/3))]

	tform = similarityTransform(eyecornerSrc, eyecornerDst)
	imOut = np.zeros(imIn.shape, dtype = imIn.dtype)

	imOut cv2.warpAffine(imIn, tform, (w,h))
	points2 = np.reshape(pointsIn,(pointsIn.shape[0],1,pointsIn.shape[1]))
	pointsOut = cv2.transform(points2,tform)
	pointsOut = np.reshape(pointsOut,(pointsIn.shape[0], pointsIn.shape[1]))
	return imOut, pointsOut
	
