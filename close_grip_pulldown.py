import cv2
import numpy as np
import time
import PoseModule as pm
import math

def close_grip_pulldown(video_path):

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
            angle_left_side_elbow = detector.findAngle(img, 12, 14, 16)
            angle_left_side_shoulder = detector.findAngle(img, 24, 12, 14)
            per_left_elbow = np.interp(angle_left_side_elbow, (167, 55), (0, 100))
            per_left_shoulder = np.interp(angle_left_side_shoulder, (200, 330), (0, 100))

            # check for pullups
            if ((per_left_elbow >= 50) and (per_left_shoulder >= 50)) and attempted_dir == 0:
                attempted_reps += 0.5
                attempted_dir = 1
            if ((per_left_elbow < 50) and (per_left_shoulder < 50)) and attempted_dir == 1:
                attempted_reps += 0.5
                attempted_dir = 0
            #person reached the bottom of the rep
            if per_left_elbow == 100 and per_left_shoulder == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
                elif attempted_dir == 0:
                    mistakes[math.ceil(attempted_reps): "did not go all the way up on rep", math.ceil(attempted_reps)]
            #person reached the top of the rep
            if per_left_elbow == 0 and per_left_shoulder == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0
                elif attempted_dir == 1:
                    mistakes[math.ceil(attempted_reps): "did not go all the way down on rep", math.ceil(attempted_reps)]


        cv2.imshow("Image", img)
        cv2.waitKey(1)

    cv2.destroyAllWindows()
    cap.release()
    # Print the count after the video has stopped playing
    if len(mistakes) != 0:
        return ("Attempted Reps: ", math.ceil(attempted_reps), "\nFinal count:", math.floor(count)), mistakes
    else:
        return "Attempted Reps: ", math.ceil(attempted_reps), "\nFinal count:", math.floor(count)

