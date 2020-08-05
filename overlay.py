import cv2
import matplotlib.pyplot as plt
from PIL import Image

class Overlay:
    
    def __init__(self,Image_Input1,Image_Input2,Input):
        self.Image_Input1=Image_Input1
        self.Image_Input2=Image_Input2
        self.Input=Input
    
    def overlay(self):
        #Here we are using add function to overlay images
        if self.Input== 1:
            img1=cv2.imread(self.Image_Input1)
            img2=cv2.imread(self.Image_Input2)
            img2_resize = cv2.resize(img2, (img1.shape[1],img1.shape[0]))
            output=cv2.add(img1,img2_resize)
            plot=plt.imshow(output)
        #Here we are using add weighted function to overlay images
        elif self.Input == 2:
            img1=cv2.imread(self.Image_Input1)
            img2=cv2.imread(self.Image_Input2)
            img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
            output = cv2.addWeighted(img1, 0.5, img2_resized, 0.3, 0)
            plot=plt.imshow(output)
        #Here we are using Image blend function
        else :
            img1=Image.open(self.Image_Input1)
            img2=Image.open(self.Image_Input2)
            img2=img2.convert(img1.mode)
            img2 = img2.resize(img1.size)
            output= Image.blend(img1,img2,0.5)
            plot=plt.imshow(output)
        return plot
    
if __name__=="__main__":
    #Here we are taking first image as input   
    Image_Input1=input('Enter the path of image1')
    #Here we are taking second image as input
    Image_Input2=input('Enter the path of image2')
    #Here we are asked to select our choice of how we want to overlay images
    Input=input('Enter how do you want to overlay Images: choices 1)Using add function 2)Using add weighted function 3)Using Image blend Enter Your choice')
    a=Overlay(Image_Input1,Image_Input2,Input)
    b=overlay()
    
        
                                                       
    