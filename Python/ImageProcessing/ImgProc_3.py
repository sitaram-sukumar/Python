import cv2;
face_cascade = cv2.CascadeClassifier(f"U:\MachineLearning\VirtualEnir\Demos\ML_Imputations\Data\DataFiles\Images\haarcascade_frontalface_default.xml");
img= cv2.imread(f"U:\\MachineLearning\\VirtualEnir\\Demos\\ML_Imputations\\Data\\DataFiles\\Images\\news.jpg");
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=15);
print(faces);
print(type(faces));

for x,y,w,h in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3);

resized = cv2.resize(img, (int(img.shape[1]/1.2), int(img.shape[1]/1.2)) );

cv2.imshow("Gray File", resized);
cv2.waitKey(0);
cv2.destroyAllWindows();