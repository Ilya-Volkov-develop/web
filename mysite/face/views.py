from django.http import StreamingHttpResponse
from django.shortcuts import render
import cv2

def face(request):
    return render(request, 'face/rgb.html')

def stream_rgb():
    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
        image_bytes = cv2.imencode('.jpg', hsv)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')  

def video_rgb(request):
    return StreamingHttpResponse(stream_rgb(), content_type='multipart/x-mixed-replace; boundary=frame')  
