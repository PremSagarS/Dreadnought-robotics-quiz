import cv2
 
cap = cv2.VideoCapture("marshmallow.webm")
 
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS)
 
path = "SlowedVideo.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(path, fourcc, 2,
                         (width, height))
 
while True:
    ret, frame = cap.read()
    output.write(frame)
    if ret == False:
        break
 
cap.release()
output.release()
cv2.destroyAllWindows()