import sys
import cv2
import os
import PIL
from PIL import Image


class squeezer:
    def __init__(self):
        print('**SQUEEZE**')
    def image(self, file):
        print('image size before compression: ' + str(os.stat(file).st_size))
        filepath = os.path.join(os.getcwd(),  
                            file) 
        picture = Image.open(filepath) 
        #saves as seperate file
        picture.save("Compressed_"+file,  
                    "JPEG",  
                    optimize = True,  
                    quality = 10)
        newfile = ('Compressed_' + file)
        print('image size before compression: ' + str(os.stat(newfile).st_size))    
        return
