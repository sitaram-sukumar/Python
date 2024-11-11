import numpy as np;
import cv2;
im1 = cv2.imread(f"S:\\Jupyter\\Files\\Data\\FamPic.JPG",1);
print(im1.shape);

aResize = im1[70:270, 100:270];
im1_resize = np.vstack((aResize,aResize,aResize));
iRetVal = cv2.imwrite(f"FamPic_New_Hstack.JPG", im1_resize);
print(iRetVal);

im2_resize = np.vstack((aResize,aResize,aResize,aResize));
iRetVal = cv2.imwrite("Fam_VStack.jpg", im2_resize);
print(iRetVal);

lst_New = np.hsplit(im1, 80)
print(lst_New[3:5]);