import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
  _, img = cap.read()
  img = cv2.resize(img,(640,350))

  org_img = img.copy()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  _,thres = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

  edges = cv2.Canny(img,100,200)

  cont,_ = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  image = cv2.drawContours(img,cont, -1,(0,255,0),2)

  edges_3d = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
  thres_3d = cv2.cvtColor(thres, cv2.COLOR_GRAY2BGR)

  np_hroz1 = np.hstack(( thres_3d, edges_3d))
  np_hroz2 = np.hstack(( image, org_img))

  final = np.vstack((np_hroz1, np_hroz2))

  cv2.imshow('couple',final)

  if cv2.waitKey(1) == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()