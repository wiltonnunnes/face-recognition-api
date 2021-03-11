import cv2 as cv
import numpy as np

def detect(image):
  image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
  image_gray = cv.equalizeHist(image_gray)

  faces = face_cascade.detectMultiScale(image_gray)
  return faces

face_cascade = cv.CascadeClassifier()
face_cascade.load('C:/Users/WillNunnes/Miniconda3/pkgs/libopencv-4.5.0-py39_3/Library/etc/haarcascades/haarcascade_frontalface_alt.xml')

cap = cv.VideoCapture(0)
if not cap.isOpened():
  print("Cannot open camera")
  exit()
while True:
  ret, frame = cap.read()

  if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    break

  faces = detect(frame)
  for (x, y, w, h) in faces:
    center = (x + w // 2, y + h // 2)
    frame = cv.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)

  cv.imshow('frame', frame)

  key = cv.waitKey(1)
  if key == ord('q'):
    break
    

cap.release()
cv.destroyAllWindows()