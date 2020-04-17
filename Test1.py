# objects1 = [{'RXBC_SHINY_CF': 98.98}, {'RXBC_TOUCH_AUD/NAV': 80.1}, {'RXBC_PWR_WDW_SW': 99.98}, {'RXBC_BL_ARR': 99.94},
#  {'RXBC_PWR_WDW_SW': 99.93}, {'RXBC_AP_PWR_WDW_SW': 99.92}, {'RXBC_SHINY_STWH': 99.03}, {'RXBC_CTINT_AV': 90.62}, 
#  {'RXBC_CTINT_AV': 88.71}, {'RXBC_CTINT_AV': 99.37}, {'RXBC_SHINY_STWH': 95.7}, {'RXBC_SHINY_CF': 93.1},
#   {'RXBC_SHINY_CF': 91.63}, {'RXBC_SHINY_STWH': 85.09}, {'RXBC_ALU_STWH': 69.89}, {'RXBC_NO_STR_SW': 64.22}]

# objects = [{'RXBC_PWR_WDW_SW': 99.98}, {'RXBC_PWR_WDW_SW': 99.93}, {'RXBC_PWR_WDW_SW': 99.99},  {'RXBC_CTINT_AV': 90.62}, 
#  {'RXBC_CTINT_AV': 88.71}, {'RXBC_CTINT_AV': 99.37},  {'RXBC_SHINY_CF': 93.1}, {'RXBC_SHINY_CF': 91.63}]

# result = []
# import dummy as tf
# dictionary = {}

# for obj in objects:
#     for key,val in obj.items():
#         if key in dictionary:
#             if (val > dictionary[key]):
#                 dictionary[key] = val
#         else:
#             dictionary[key] = val
# # print(dictionary)
# for key, val in dictionary.items():
#     result.append(key + "~" + str(val))


# data = {"output" : result}
# print(data)

# from PIL import Image
# import pytesseract
# import cv2
# import matplotlib.pyplot as plt

# tessdata_dir_config = '--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata"'
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

# image = cv2.imread("C:/Users/z014417/Downloads/Char Detection/opencv-text-detection/images/image4.jpg")


# gray = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# (thresh, blackAndWhiteImage) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow('Black white image', blackAndWhiteImage)
# cv2.imshow('Original image',image)
# cv2.imshow('Gray image', gray)

# originaltext = pytesseract.image_to_string(image)
# blackwhitetext = pytesseract.image_to_string(blackAndWhiteImage)
# graytext = pytesseract.image_to_string(gray)

# print("originaltext value which we identified is ", originaltext)
# print("blackwhitetext value which we identified is ", blackwhitetext)
# print("graytext value which we identified is ", graytext)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

objects =  [{ "RXBC_PWR_WDW_SW" : 98.67 } ,{ "RXBC_FAB_ARR" : 98.67 } ,{ "RXBC_PB_PHND" : 98.67 } ,{ "RXBC_BLACK_MIRROR" : 98.67 } ,
    { "RXBC_MANUAL_AUD/NAM" : 98.67 } ,{ "RXBC_NO_UGLB" : 98.67 } ,{ "RXBC_NO_LGLB" : 98.67 } ,{ "RXBC_TINT_AV" : 98.67 } ,
    { "RXBC_TINT_TD" : 98.67 } ,{ "RXBC_TRIP_SW"  : 98.67 } ]

result = []
for obj in objects:
    for val in obj:
        result.append(val +"~" +str(obj[val]))

data = {"objectList" : result} 
print(data) 
