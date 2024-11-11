import cv2;
import os;

def ProcessResizingFiles(dirPath):
    if not os.path.exists(os.path.join(dirPath,"resizedImages")):
        os.mkdir(os.path.join(dirPath,"resizedImages"));
        
    for fileName in os.listdir(dirPath):
        fullFileName = os.path.join(dirPath, fileName);
        if os.path.isfile(fullFileName):
            print(fullFileName);
            img = cv2.imread(fullFileName);
            img_resize = cv2.resize(img, (100,100));
            iRetVal = cv2.imwrite(os.path.join(dirPath+"\\resizedImages", fileName), img_resize);
            print(iRetVal);

ProcessResizingFiles("U:\MachineLearning\VirtualEnir\Demos\ML_Imputations\Data\DataFiles\Images\\");