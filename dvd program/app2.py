import cv2
import numpy as np
import random
from flask import Flask, Response, render_template
import time

app = Flask(__name__)

def generateRandomColor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

width = 1000
height = 600
text = "DVD"
textFont = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.7
thickness = 2

# Initialize position and movement variables
x = 200
y = 200
dx = 8
dy = 6

def generate_frame():
    global x, y, dx, dy
    
    # Create a black image
    blackImage = np.zeros((height, width, 3), dtype=np.uint8)
    color = generateRandomColor()

    while True:
        # Clear the image
        blackImage[:] = 0
        
        # Draw the text
        cv2.putText(blackImage, text, (x, y), textFont, fontScale, color, thickness, cv2.LINE_AA)
        
        # Convert the image to a format suitable for display in the browser
        _, jpeg = cv2.imencode('.jpg', blackImage)
        frame = jpeg.tobytes()

        # Update position
        x += dx
        y += dy
        
        # Check for boundary collisions
        if x + len(text) * 15 > width or x < 0:
            dx = -dx
            color = generateRandomColor()
        if y + 80 > height or y < 100:
            dy = -dy
            color = generateRandomColor()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
