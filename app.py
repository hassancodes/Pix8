import cv2 as cv
from flask import Flask, flash,render_template,redirect,Response,request, send_from_directory,url_for
from werkzeug.utils import secure_filename
from camera import Camera
from imgconv import convert_to_8bit
import os
import time


save_image=True
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




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



# Gallery Starts from here

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")
    


############### Upload functionality starts from here ########################
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # call the function here to manipulate the image here
            time.sleep(2)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            convert_to_8bit(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            time.sleep(2)
            return redirect(url_for('uploaded_file',filename=filename))
            # return redirect(url_for('uploaded_file',filename=filename))
            # return redirect("/upload")
            # return ("HELLO")
    return render_template("convert.html")
    
    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    print(filename)
    # print(app.config['UPLOAD_FOLDER'].join())
    return render_template("converted.html",address=filename)


    # return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
    







if __name__ == "__main__":
    app.run(debug=True)