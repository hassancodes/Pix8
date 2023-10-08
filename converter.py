# import cv2
# import skimage as ski
# from camera import Camera



# cam = cv2.VideoCapture("landscape.mp4")
# w, h = (128, 128)


# while cam.isOpened():
#     check, frame = cam.read()
    
#     grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     grey = cv2.medianBlur(grey, 5)
#     edges = cv2.adaptiveThreshold(grey, 256, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

#     #cartoonize
#     color = cv2.bilateralFilter(frame, 15, 255, 255)
#     cartoon = cv2.bitwise_and(color, color, mask = edges)
#     frame1 = cv2.resize(cartoon, (w, h), interpolation=cv2.INTER_LINEAR)
#     final = cv2.resize(frame1, (540, 960), interpolation=cv2.INTER_NEAREST)
    
#     cv2.imshow('Pix8', final)

#     key = cv2.waitKey(1)
#     if key == 27:
#         break

# cam.release()
# cv2.destroyAllWindows()



