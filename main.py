import cv2
import numpy as np
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0)

poseDetector = PoseDetector()
count = 0
direction = 0

workout = "push-up"  # "curl", "squat"

while True:
    success, flip = cap.read()
    img = cv2.flip(flip, 1)
    img = poseDetector.findPose(img)
    lmList, bbox = poseDetector.findPosition(img, draw=False)
    if lmList:
        if workout == "squat":
            p1 = 23
            p2 = 25
            p3 = 27
            xp = (70, 160)
            fp_per = (100, 0)
            fp_bar = (100, 650)
        else:
            p1 = 11
            p2 = 13
            p3 = 15
            fp_per = (0, 100)
            fp_bar = (650, 100)
            xp = (210, 310)

        angle = poseDetector.findAngle(img, p1, p2, p3)
        per = np.interp(angle, xp, fp_per)
        bar = np.interp(angle, xp, fp_bar)

        if per == 100:
            if direction == 0:
                count += 0.5
                direction = 1
        if per == 0:
            if direction == 1:
                count += 0.5
                direction = 0

        cv2.rectangle(img, (1100, 100), (1175, 650), (0, 255, 0), 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f"{int(per)}%", (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 4)

        cv2.rectangle(img, (0, 458), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15, (255, 0, 0), 25)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
