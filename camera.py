import cv2 as cv

# main class that process the images and then send it over to the flask server in app.py
class Camera(object):
    def __init__(self):
        self.video = cv.VideoCapture("landscape.mp4");
        self.current =None
        self.count =True
    
    def __del__(self):
        self.video.release()
        
    def get_frame(self):
        ret,frame =self.video.read();        
        grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        grey = cv.medianBlur(grey, 5)
        edges = cv.adaptiveThreshold(grey, 256, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)

        #cartoonize
        color = cv.bilateralFilter(frame, 15, 255, 255)
        cartoon = cv.bitwise_and(color, color, mask = edges)
        w,h = 128,128
        frame1 = cv.resize(cartoon, (w, h), interpolation=cv.INTER_LINEAR)
        final = cv.resize(frame1, (480, 270), interpolation=cv.INTER_NEAREST)

        ret,jpeg = cv.imencode(".jpg",final)
        # cv.imshow('Pix8', final)
        self.current= final
        # cv.imwrite("frame%d.jpg" % 0, jpeg)
        return jpeg.tobytes();
    
    def down_image(self):
        if self.count==True:
            print("This  is self #########################")
            cv.imwrite("static/frame.jpg" , self.current)
            print(self.current)
            self.count==False
        else:
            pass
    
    
        