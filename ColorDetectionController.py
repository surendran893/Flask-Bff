import cv2
import numpy as np
import pandas as pd

class Color_Detection(object):

    #Global variable for Color Detection
    r = g = b = xpos = ypos = 0
    img = None

    def getColorName(R,G,B):

        #Reading csv file with pandas and giving names to each column
        index=["color","color_name","hex","R","G","B"]
        csv = pd.read_csv('colors.csv', names=index, header=None) 

        minimum = 10000
        for i in range(len(csv)):
            d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
            if(d<=minimum):
                minimum = d
                cname = csv.loc[i,"color_name"]
        return cname

    #function to get x,y coordinates of mouse double click
    def draw_function(x,y):
        global b,g,r,xpos,ypos
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

    def detect_Color(imgPath):
        global img, csv
        img = cv2.imread(imgPath)

        Color_Detection.draw_function(933, 555)

        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Creating text string to display( Color name and RGB values )
        text = Color_Detection.getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)

        print("color value is ", text) 

main = Color_Detection

color_name = main.detect_Color("C:/Users/z014417/Downloads/colro detection/blue.jpg")