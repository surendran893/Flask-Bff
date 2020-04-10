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

import os

IMG_PATH = "C:/Workspace/Machine Learning Project/Images/Test Images"

print(os.listdir(IMG_PATH)[0])