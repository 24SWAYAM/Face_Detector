import cv2
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 420)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.3, 5) 
    eyes = eyeCascade.detectMultiScale(imgGray, 1.3, 5)
    smile = smileCascade.detectMultiScale(imgGray, 1.3, 5)
    for (x, y, w, h) in smile:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.imshow('face_detect', img)
    for (x, y, w, h) in eyes:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.imshow('face_detect', img)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.imshow('face_detect', img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
