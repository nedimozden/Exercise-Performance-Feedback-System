import exerciseFiles
import cv2
import numpy as np
import time
import math
import PoseModule as pm
from exerciseFiles.pullup import pullup
from exerciseFiles.back_extension import back_extension
from exerciseFiles.bent_over_barbell_row import bent_over_barbell_row
from exerciseFiles.deadlift import deadlift
from exerciseFiles.cable_rope_pullover import cable_rope_pullover
from exerciseFiles.close_grip_pulldown import close_grip_pulldown
from exerciseFiles.face_pull import facepull
from tkinter import filedialog
import tkinter as tk


def upload_local_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("MOV files", "*.mov")])

    return file_path

if __name__ == "__main__":

    # Prompt the user to upload a .MOV file
    mov_file_path = upload_local_file()

    if mov_file_path:
        print(f"File uploaded: {mov_file_path}")
        # Now you can process the uploaded .MOV file using your desired logic.
    else:
        print("No file selected.")

    # Prompt the user for the video file path
    exercise_called = input("Enter the number corresponding to the exercise you want advice on from the following options: \npullup = 1\nback_extension = 2\nbent_over_barbell_row = 3\n"
                            "\ncable_rope_pullover = 4\nclose_grip_pulldown = 5\ndeadlift = 6\nfacepull = 7\n: ")


    # Call the function with the provided video path
    if exercise_called == "1":
        pullup(mov_file_path)
    if exercise_called == "2":
        back_extension(mov_file_path)
    if exercise_called == "3":
        bent_over_barbell_row(mov_file_path)
    if exercise_called == "4":
        cable_rope_pullover(mov_file_path)
    if exercise_called == "5":
        close_grip_pulldown(mov_file_path)
    if exercise_called == "6":
        deadlift(mov_file_path)
    if exercise_called == "7":
        facepull(mov_file_path)
        
