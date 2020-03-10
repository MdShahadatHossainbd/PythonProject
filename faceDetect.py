import cv2
from datetime import datetime
first_frame = None
status_list = [None, None]
times = []
camera_port = 0
camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
video = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
return_value, img = camera.read()
while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    key = cv2.waitKey(1)
    if key == ord('s'):
        break

    if first_frame is None:
        first_frame = gray
        if key == ord('s'):
            break
        continue
    status = 1

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)
    contours, hierarchy = cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            if key == ord('s'):
                break
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        text = "Detected motion in the room"
        face_cascade = cv2.CascadeClassifier("C:\\Users\\shaha\\PycharmProjects\\cv3\\haarcascade_frontalface_default.xml")
        eye_cascade = cv2.CascadeClassifier("C:\\Users\\shaha\\PycharmProjects\\cv3\\haarcade_eye.xml")
        if face_cascade.empty():  raise IOError('Unable to load the face cascade classifier xml file')
        if eye_cascade.empty():  raise IOError('Unable to load the eye cascade classifier xml file')
        face = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
        #key = cv2.waitKey(1)
        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (x_eye, y_eye, w_eye, h_eye) in eyes:
                center = (int(x_eye + 0.5 * w_eye), int(y_eye + 0.5 * h_eye))
                radius = int(0.3 * (w_eye + h_eye))
                color = (100, 280, 0)
                thickness = 5
                cv2.circle(roi_color, center, radius, color, thickness)
        resized = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())

    if status_list[-1] == 1 and status_list[-2] == 1:
        times.append(datetime.now())
        return_value, img = camera.read()
        cv2.imwrite("geng.jpg", img)

    cv2.imshow('frame', frame)
    cv2.imshow('delta', delta_frame)
    c = cv2.waitKey(1)
    if c == 27:
        break

print(status_list)
print(times)

video.release()
cv2.destroyAllWindows()
