# project_final_image
## Watch our ![demo video](https://drive.google.com/file/d/1qZ3rjKE7sBuCKIQGI06jxRt5-xIrL3up/view?usp=sharing)
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
## 4. move to "sobel and laplacian" tab.
## 5. insert the kernal size that is used for sobel detection
![](screen_shots/image_3.png)
## 6. press sobel button, the pop window will show for you, you can choose from the combo box the direction that you want to calculate sobel in it ( X or Y or XY).
![](screen_shots/image_4.png)
![](screen_shots/image_5.png)
![](screen_shots/image_6.png)
![](screen_shots/image_7.png)
## 7. if you change the kernal size to 3.
![](screen_shots/image_8.png)
![](screen_shots/image_9.png)
![](screen_shots/image_10.png)
## 8. press the laplacian button, also the pop window will show for you with calculated laplace edge detection for the image.
![](screen_shots/image_11.png)
## 9. move to "fourier, add noise and remove it" tab.
![](screen_shots/image_12.png)
## 10. choose from the combo box which type from noise that you want to add and then once you choose the type, the noisy image will be displayed with its fourier for you.
## - gaussian noise:
![](screen_shots/image_13.png)
## - choose gaussian filter from "remove noise combo box", the filtered image and its fourier will be displayed for you.
![](screen_shots/image_14.png)
![](screen_shots/image_15.png)
## - salt and paper noise: you should insert the amount of salt and paper that you want to be added.
![](screen_shots/image_16.png)
![](screen_shots/image_17.png)
## - choose median filter from "remove noise combo box", the filtered image and its fourier will be displayed for you.
![](screen_shots/image_18.png)
## 11. move to "add periodic noise and remove it" tab.
![](screen_shots/image_19.png)
## 12. press "add periodic noise button".
![](screen_shots/image_20.png)
## 13. select type of filter that you want to remove periodic noise from the combo box.
![](screen_shots/image_21.png)
## 14. if you choose band reject filter, the filtered image and its fourier will be displayed for you.
![](screen_shots/image_22.png)
## 15. if you choose mask method for remove periodic noise, the pop window, contains the fourier of the periodic noise image, will be displayed for you.
![](screen_shots/image_23.png)
## 16. then by mouse click, select the pixels that you want to suppress in fourier transform.
![](screen_shots/image_24.png)
## 17. then press any key from keyboard, to out from this pop window.
## 18. after that, the filtered image and its fourier will be displayed for you.
![](screen_shots/image_25.png)
