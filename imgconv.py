import cv2
import asyncio 
def convert_to_8bit(file_name):
    image = cv2.imread(file_name)

    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grey = cv2.medianBlur(grey, 5)
    edges = cv2.adaptiveThreshold(grey, 256, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(image, 15, 255, 255)
    cartoon = cv2.bitwise_and(color, color, mask = edges)
    frame1 = cv2.resize(cartoon, (100, 100), interpolation=cv2.INTER_LINEAR)
    final = cv2.resize(frame1, (image.shape[0]//2, image.shape[0]//2), interpolation=cv2.INTER_NEAREST)
    print(file_name)
    cv2.imwrite(file_name,final)


# conv_img("static/av1.jpg")



























# import cv2 
# image = cv2.imread('av1.jpg')
# print(image.shape)

# grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# grey = cv2.medianBlur(grey, 5)
# edges = cv2.adaptiveThreshold(grey, 256, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
# color = cv2.bilateralFilter(image, 15, 255, 255)
# cartoon = cv2.bitwise_and(color, color, mask = edges)
# frame1 = cv2.resize(cartoon, (100, 100), interpolation=cv2.INTER_LINEAR)
# final = cv2.resize(frame1, (image.shape[0]//2, image.shape[0]//2), interpolation=cv2.INTER_NEAREST)

# cv2.imshow('Pix8', final)

# cv2.waitKey(0)   
# cv2.destroyAllWindows()