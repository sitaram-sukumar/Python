import cv2;
img = cv2.imread('U:\\MachineLearning\\VirtualEnir\\Demos\\ML_Imputations\\Data\\DataFiles\\ImageProcFIles\\galaxy.jpg', 0)
print(type(img));
print(img);
print(img.shape);
print(img.ndim);

reImg = cv2.resize(img, (int(img.shape[0]/1.5),int(img.shape[1]/1.5)) );

cv2.imshow("New Galaxy", reImg);
#cv2.waitKey(5000);
#cv2.destroyAllWindows();

cv2.waitKey(0);
cv2.destroyAllWindows();