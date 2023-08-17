import cv2

cap = cv2.VideoCapture("marshmallow.webm")

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS)

path = "ReversedVideo.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(path, fourcc, 2,
                         (width, height))

check , vid = cap.read()
counter = 0
check = True  
frame_list = []

while(check == True):
    check , vid = cap.read()
    frame_list.append(vid)
    counter += 1

frame_list.pop()

frame_list.reverse()
  
for frame in frame_list:
    output.write(frame)
  
cap.release()
cv2.destroyAllWindows()