import cv2 as cv
from flask import Flask,render_template,redirect,Response
from camera import Camera
from dotenv import load_dotenv
load_dotenv()
import os
print(os.getenv('BUTTON_CLICKED'))
import time


app = Flask(__name__)

save_image=True
@app.route("/")
def Home():
    global save_image
    if save_image:
        save_image=False
    elif save_image==False:
        save_image==True
    
    return render_template("index.html")    

def gen(camera):

    while True:
        
        global frame
        frame= camera.get_frame()
        if save_image==False:
            camera.down_image()
        else:
            pass
        
        yield(b'--frame\r\n'
              b'Content-Type:image/jpeg\r\n\r\n' + frame
              + b"\r\n\r\n")



    
@app.route("/video_feed")
def video_feed():
    return Response(gen(Camera()), mimetype="multipart/x-mixed-replace;boundary=frame")



    

    







if __name__ == "__main__":
    app.run("localhost",debug=True)