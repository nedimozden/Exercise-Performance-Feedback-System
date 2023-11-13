import cv2
import numpy as np
import time
import PoseModule as pm
import math



def pullup(video_path):
    cap = cv2.VideoCapture(video_path)
    detector = pm.poseDetector()
    count = 0
    attempted_reps = 0
    attempted_dir = 0
    dir = 0
    mistakes = {}
    while True:
        success, img = cap.read()

        if not success:
            break  # Break the loop when all frames are read

        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)

        if len(lmList) != 0:
            angle_right_side_elbow = detector.findAngle(img, 12, 14, 16)
            angle_left_side_elbow = detector.findAngle(img, 11, 13, 15)
            per_right = np.interp(angle_right_side_elbow, (45, 140), (0, 100))
            per_left = np.interp(angle_left_side_elbow, (210, 310), (0, 100))
            x1, y1 = lmList[16][1:]
            x2, y2 = lmList[12][1:]

            # check for pullups
            if y1 < y2:
                if ((per_right >= 50) and (per_left <= 50)) and attempted_dir == 0:
                    attempted_reps += 0.5
                    attempted_dir = 1
                if ((per_right < 50) and (per_left > 50)) and attempted_dir == 1:
                    attempted_reps += 0.5
                    attempted_dir = 0
                # person reached the bottom of the rep
                if per_right == 100 and per_left == 0:
                    if dir == 0:
                        count += 0.5
                        dir = 1
                    elif attempted_dir == 0:
                        mistakes[math.ceil(attempted_reps): "did not go all the way up on rep",
                        math.ceil(attempted_reps)]
                # person reached the top of the rep
                if per_right == 0 and per_left == 100:
                    if dir == 1:
                        count += 0.5
                        dir = 0
                    elif attempted_dir == 1:
                        mistakes[math.ceil(attempted_reps): "did not go all the way down on rep",
                        math.ceil(attempted_reps)]

        cv2.imshow("Image", img)
        cv2.waitKey(1)

    cv2.destroyAllWindows()
    cap.release()
    # Print the count after the video has stopped playing
    if len(mistakes) != 0:
        print("Attempted Reps: ", math.ceil(attempted_reps), "\nFinal count:", math.floor(count))
        print(mistakes)
    else:
        print("Attempted Reps: ", math.ceil(attempted_reps), "\nFinal count:", math.floor(count))


