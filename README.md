# project_final_image

## How to work:
## 1. load the image
## 2. if the user press on calcuate histogram button:
## - in the backend of the gui, the image is converted to grayscale.
## - after that the histogram is calculated for it using opencv.
## - finally, the histogram will show for the user.
![](screen_shots/image_1.png) 

## 3. Eqalize the image:
## - if equalize button is pressed, the image is converted to YCrCb.
## - then equalize the hitogram of the Y channel
## - convert back to RGB color-space from YCrCb.
## - press calculate equalize histogram button, to show histogram of equalized image.
![](screen_shots/image_2.png)
## 4. insert the kernal size that is used for sobel detection
![](screen_shots/image_3.png)
## 5. press sobel button, the pop window will show for you, you can choose from the combo box the direction that you want to calculate sobel in it ( X or Y or XY).
![](screen_shots/image_4.png)
![](screen_shots/image_5.png)
![](screen_shots/image_6.png)
![](screen_shots/image_7.png)
## 6. if you change the kernal size to 3.
![](screen_shots/image_8.png)
![](screen_shots/image_9.png)
![](screen_shots/image_10.png)
## 7. press the laplacian button, also the pop window will show for you with calculated laplace edge detection for the image.
![](screen_shots/image_11.png)