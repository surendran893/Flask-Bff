import cv2
import numpy as np
import pandas as pd

class Color_Detection(object):

    #Global variable for Color Detection
    r = g = b = xpos = ypos = 0

    def getColorName(R,G,B):

        #Reading csv file with pandas and giving names to each column
        index=["color","color_name","hex","R","G","B"]
        csv = pd.read_csv('C:/Workspace/Machine Learning Project/Python_Flask_Bff/Flask-Bff/colors.csv', names=index, header=None) 

        minimum = 10000
        for i in range(len(csv)):
            d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
            if(d<=minimum):
                minimum = d
                cname = csv.loc[i,"color_name"]
        return cname

    #function to get x,y coordinates of mouse double click
    def draw_function(x,y, imgPath):
        img = cv2.imread(imgPath)
        global b,g,r
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
        return img

    def detect_Color(imgPath):
        # img = cv2.imread(imgPath)
        print(imgPath)

        img = Color_Detection.draw_function(937, 555, imgPath)

        #Creating text string to display( Color name and RGB values )
        text = Color_Detection.getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)

        color_value = Color_Detection.getColorName(r,g,b)
        print("color value is ", text) 

        return color_value
