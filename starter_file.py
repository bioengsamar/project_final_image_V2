from PyQt5 import QtWidgets
from designs.design import Ui_MainWindow
from designs.sobel import Ui_ui_main
from designs.laplace import Ui_ui_mainwindow
from skimage.util import random_noise
from  PyQt5.QtWidgets  import QFileDialog, QMessageBox 
from PyQt5.QtGui import QPixmap,QImage, QColor
import cv2
import numpy as np
import sys


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.window= QtWidgets.QMainWindow()
        self.u= Ui_ui_main()
        self.u.setupUi(self.window)
        self.window2= QtWidgets.QMainWindow()
        self.uu= Ui_ui_mainwindow()
        self.uu.setupUi(self.window2)
        self.u.comboBox.currentTextChanged.connect(self.sobel)
        self.ui.comboBox.currentTextChanged.connect(self.add_noise)
        self.ui.comboBox_2.currentTextChanged.connect(self.remove_noise)
        self.ui.comboBox_3.currentTextChanged.connect(self.remove_periodic_noise)
        
    def load(self):
        global img_1
        self.file1 = QFileDialog.getOpenFileName(self, 'Open file','',' *.jpg *.png')[0]
        img_1 = cv2.imread(self.file1)
        image1 = QPixmap(self.file1)
        self.ui.label.setPixmap(QPixmap(image1.scaled(301,201)))
        
        
    def calculate_histogram(self, img):
        self.gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        counts, bins = np.histogram(self.gray, range(257))
        return bins, counts
            
    def draw_histogram(self):
        bins, counts = self.calculate_histogram(img_1)
        self.ui.MplWid2.canvas.axes.plot(bins[:-1] - 0.5, counts)
        self.ui.MplWid2.canvas.axes.set_xlabel('pixels values')
        self.ui.MplWid2.canvas.axes.set_ylabel('Pixels')
        self.ui.MplWid2.canvas.draw()
        
    def equalize_histogram(self):
        global equalized_img
        # convert from RGB color-space to YCrCb
        ycrcb_img = cv2.cvtColor(img_1, cv2.COLOR_BGR2YCrCb)
    
        # equalize the histogram of the Y channel
        ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])
    
        # convert back to RGB color-space from YCrCb
        equalized_img = cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)
        result = cv2.imwrite('outputs/equalized_img.jpg', equalized_img)
        result = QPixmap("outputs/equalized_img.jpg").scaled(301,201)
        self.ui.label_2.setPixmap(QPixmap(result))
        
    def draw_equalize_histo(self):
        bins, counts = self.calculate_histogram(equalized_img)
        self.ui.MplWid2_2.canvas.axes.plot(bins[:-1] - 0.5, counts)
        self.ui.MplWid2_2.canvas.axes.set_xlabel('pixels values')
        self.ui.MplWid2_2.canvas.axes.set_ylabel('Pixels')
        self.ui.MplWid2_2.canvas.draw()
        
    def getPos(self , event):
        global points
        points = []
        x = event.pos().x()
        y = event.pos().y()
        print(x,',',y)
        points.append([x,y])
        
    def sobel_(self, img, sobelx=False, sobely= False, ksize=0):
        if sobelx:
            sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=ksize)  # x
            return sobelx
        if sobely:
            sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=ksize)  # y
            return sobely
        
    def sobel(self):
        mg = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
        text = self.ui.textEdit.toPlainText()
        
        if self.u.comboBox.currentText()=='X':
            sobel = self.sobel_(mg, sobelx=True, ksize= int(text))
        if self.u.comboBox.currentText()=='Y':
            sobel = self.sobel_(mg, sobely=True, ksize= int(text))
            
        if self.u.comboBox.currentText()=='XY':
            sobel = np.sqrt(np.square(self.sobel_(mg, sobelx=True, ksize= int(text))) + np.square(self.sobel_(mg, sobely=True, ksize= int(text)) ))
            sobel *= 255.0 / sobel.max()
        
        sobel_img = cv2.imwrite('outputs/sobel_img.jpg', sobel)
        sobel_img = QPixmap("outputs/sobel_img.jpg").scaled(301,201)
        self.u.label_3.setPixmap(QPixmap(sobel_img))
        
    def show_sobel_window(self):
        self.window.show()
        
    def show_laplace_window(self):
        self.window2.show()
        img = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
        laplacian = cv2.Laplacian(img,cv2.CV_64F)
        laplacian_img = cv2.imwrite('outputs/laplacian_img.jpg', laplacian)
        laplacian_img = QPixmap("outputs/laplacian_img.jpg").scaled(301,201)
        self.uu.label.setPixmap(QPixmap(laplacian_img))
    
    def Fourier(self, img):
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20*np.log(np.abs(fshift))
        return magnitude_spectrum, fshift
        
        
        
    def add_noise(self):
        global noise_img
        if self.ui.comboBox.currentIndex()==2: #gaussian
            noise_img = random_noise(img_1, mode='gaussian')
            noise_img = np.array(255*noise_img, dtype = 'uint8')
            
        if self.ui.comboBox.currentText()=='salt and paper':
            noise_img = random_noise(img_1, mode='s&p',amount=0.1)
            noise_img = np.array(255*noise_img, dtype = 'uint8')
            
        magnitude_spectrum = self.Fourier(noise_img)[0]
        Fourier_img = cv2.imwrite('outputs/magnitude_spectrum.jpg', magnitude_spectrum)
        Fourier_img = QPixmap("outputs/magnitude_spectrum.jpg").scaled(301,201)
        self.ui.label_3.setPixmap(QPixmap(Fourier_img))
        noise_image = cv2.imwrite('outputs/noise_img.jpg', noise_img)
        noise_image = QPixmap("outputs/noise_img.jpg").scaled(301,201)
        self.ui.label_4.setPixmap(QPixmap(noise_image))
        
    def remove_noise(self):
        if self.ui.comboBox_2.currentText()=='median filter':
            filtered = cv2.medianBlur(noise_img, 3)
            
        if self.ui.comboBox_2.currentText()=='gaussian filter':
            filtered = cv2.fastNlMeansDenoisingColored(noise_img,None,10,10,7,21)
            
        magnitude_spectrum = self.Fourier(filtered)[0]
        Fourier_img = cv2.imwrite('outputs/magnitude_spectrum.jpg', magnitude_spectrum)
        Fourier_img = QPixmap("outputs/magnitude_spectrum.jpg").scaled(301,201)
        self.ui.label_9.setPixmap(QPixmap(Fourier_img))
        filtered_img = cv2.imwrite('outputs/filtered_img.jpg', filtered)
        filtered_img = QPixmap("outputs/filtered_img.jpg").scaled(301,201)
        self.ui.label_5.setPixmap(QPixmap(filtered_img))
    
    def Add_periodic_noise(self):
        global noiseada
        orig = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
        sh = orig.shape[0], orig.shape[1]
        noise = np.zeros(sh, dtype='float64')
        
        X, Y = np.meshgrid(range(0, sh[1]), range(0, sh[0]))
        
        A = 50
        u0 = 50
        v0 = 50
        
        noise += A*np.sin(X*u0 + Y*v0)
        
        A = -18
        u0 = -45
        v0 = 50
        
        noise += A*np.sin(X*u0 + Y*v0)
        noiseada = orig+noise
        noiseada_img = cv2.imwrite('outputs/noiseada_img.jpg', noiseada)
        noiseada_img = QPixmap("outputs/noiseada_img.jpg").scaled(391,341)
        self.ui.label_6.setPixmap(QPixmap(noiseada_img))
        #magnitude_spectrum = self.Fourier(noiseada)[0]
        #Fourier_img = cv2.imwrite('outputs/noiseada_spectrum.jpg', magnitude_spectrum)
        #Fourier_img = QPixmap("outputs/noiseada_spectrum.jpg").scaled(1091,781)
        #self.ui.label_8.setPixmap(QPixmap(Fourier_img))
        #self.ui.label_8.mousePressEvent = self.getPos
        
    def click_mouse(self, spectrum):
        global points
        points = []
        def click_event( event, x, y, flags, params):
            	
            	
            	# checking for left mouse clicks
            	if event == cv2.EVENT_LBUTTONDOWN:
            
            		# displaying the coordinates
            		# on the Shell
            		#print(x, ' ', y)
            
            		# displaying the coordinates
            		# on the image window
            		points.append((y,x))
            		font = cv2.FONT_HERSHEY_SIMPLEX
            		cv2.putText(image, str(x) + ',' +
            					str(y), (x,y), font,
            					1, (255, 0, 0), 2)
            		cv2.imshow('spectrum', image)
            	
            	# checking for right mouse clicks	
            	if event==cv2.EVENT_RBUTTONDOWN:
            
            		# displaying the coordinates
            		# on the Shell
            		#print(x, ' ', y)
            
            		# displaying the coordinates
            		# on the image window
            		points.append((y,x))
            		font = cv2.FONT_HERSHEY_SIMPLEX
            		b = image[y, x, 0]
            		g = image[y, x, 1]
            		r = image[y, x, 2]
            		cv2.putText(image, str(b) + ',' +
            					str(g) + ',' + str(r),
            					(x,y), font, 1,
            					(255, 255, 0), 2)
            		cv2.imshow('spectrum', image)
            	
        cv2.imwrite('outputs/magnitude_spectrum_noise.jpg', spectrum)
        image = cv2.imread('outputs/magnitude_spectrum_noise.jpg')
        cv2.imshow('spectrum', image)
        
        # setting mouse handler for the image
        # and calling the click_event() function
        cv2.setMouseCallback('spectrum', click_event)
        
        # wait for a key to be pressed to exit
        cv2.waitKey(0)
        
        # close the window
        cv2.destroyAllWindows()
        
   
        
    def remove_periodic_noise(self):
        if self.ui.comboBox_3.currentText()=='band reject filter':
            spectrum = self.Fourier(noiseada)[1]
            rows, cols = noiseada.shape
            crow, ccol = int(rows / 2), int(cols / 2)
            
            mask1 = np.ones((rows, cols))
            mask2 = mask1.copy()
            
            center = [crow, ccol]
            x, y = np.ogrid[:rows, :cols]
            mask1_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 >= 30*30
            mask2_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 >= 60*60
            
            mask1[mask1_area] = 0
            mask2[mask2_area] = 0
            
            band_reject = np.logical_not(np.abs(mask2 - mask1) )
            fshift = spectrum*band_reject
            f_ishift= np.fft.ifftshift(fshift)
            
            img_back = np.fft.ifft2(f_ishift) 
            img_back = np.abs(img_back)
            
        if self.ui.comboBox_3.currentText()=='Mask':
            spectrum, fshift = self.Fourier(noiseada)
            
            self.click_mouse(spectrum)
            rows, cols = noiseada.shape
            mask = np.ones((rows, cols))
            print(points)
            for point in points:
                #print(point)
                mask[point] = 0
                IMFr = np.fft.ifftshift(fshift*mask)
                imfr = np.fft.ifft2(IMFr)
                img_back = np.real(imfr)
            
            #print(img_back)
        magnitude_spectrum = self.Fourier(img_back)[0]
        Fourier_img = cv2.imwrite('outputs/magnitude_spectrum.jpg', magnitude_spectrum)
        Fourier_img = QPixmap("outputs/magnitude_spectrum.jpg").scaled(281,261)
        self.ui.label_11.setPixmap(QPixmap(Fourier_img))
        filtered_img = cv2.imwrite('outputs/filtered_periodic_img.jpg', img_back)
        filtered_img = QPixmap("outputs/filtered_periodic_img.jpg").scaled(281,261)
        self.ui.label_8.setPixmap(QPixmap(filtered_img))
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()