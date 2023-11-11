from ultralytics import YOLO
import cv2
import numpy as np
import math

classnames = ['Ambulance', 'Bus', 'Car', 'Motorcycle', 'Truck']
model = YOLO(r'best.pt')
cam = cv2.VideoCapture('vehicle_vid3.mp4')

fsize = (int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = int(cam.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
output_video = cv2.VideoWriter('Result.mp4', fourcc, fps, fsize)

while True:

    ret,frame = cam.read()
    #frame = cv2.resize(frame,(640,640))
    result = model(frame, stream = True)
    for r in result:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            print(x1, y1, x2, y2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 250), 2)

            # For confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            print('Confidence of bounding box is', conf)

            # For classes
            cls = int(box.cls[0])

            cv2.putText(frame, f'{classnames[cls]} {conf}', (max(0, x1), max(40, y1)), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 255, 0), 2)

    output_video.write(frame)
    cv2.imshow("live", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('video closed')
        break


cv2.destroyAllWindows()

