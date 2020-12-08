


import numpy as np
import cv2
from flask import *  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():
    return render_template('go.html')
@app.route('/go')   
def go():
    cap = cv2.VideoCapture(0)
    if (cap.isOpened()== False):  
         print("Error opening video  file") 

    while(cap.isOpened()):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return render_template('index.html')  
  
if __name__ =='__main__':  
    app.run(debug = True)  