import os
import cv2
import shutil

width = 1920
height =1080

# For saving purposes only
counter = 0

# Open the first webcam available
cap = cv2.VideoCapture(0)

# Set the resolution of the capture frame
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Check if the webcam was successfully opened
if not cap.isOpened():
    print("Could not open webcam")
    exit()
    
os.system("echo Say cheese!")

# Capture a frame from the webcam
ret, frame = cap.read()

# Check if the frame was successfully captured
if not ret:
    print("Could not capture frame")
    exit()

# Save the captured frame to a file
cv2.imwrite("C:\\Users\\K017-Labor\\Desktop\\SetupFolder\\Screenshots\\A.jpg", frame)

source = "C:\\Users\\K017-Labor\\Desktop\\SetupFolder\\Screenshots\\A.jpg"
destination = "C:\\Users\\K017-Labor\\Desktop\\SetupFolder\\Saved_Pics\\"
new_file_name = "image_" + str(counter) + ".jpg"

counter += 1

# Use shutil.copy2() to copy the file and preserve metadata
shutil.copy(source, destination + new_file_name)


# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()