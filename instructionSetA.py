import os
import cv2

width = 1920
height =1080

# Open the first webcam available
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#cv2.VideoCapture(0)

# Set the resolution of the capture frame
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Check if the webcam was successfully opened
if not cap.isOpened():
    print("Could not open webcam")
    os.system("Could not open webcam")
    exit()
    
os.system("echo Press SPACEBAR to take a picture!")

# Keep capturing frames from the webcam until spacebar is pressed
while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Display the captured frame in a window
    cv2.imshow("Webcam", frame)

    # Wait for the user to press a key
    key = cv2.waitKey(1)

    # Check if the spacebar was pressed
    if key == ord(" "):
        # Save the captured frame to a file
        cv2.imwrite("C:\\Users\\K017-Labor\\Desktop\\SetupFolder\\Screenshots\\A.jpg", frame)

        os.system(r"magick C:\Users\K017-Labor\Desktop\SetupFolder\Screenshots\A.jpg -crop 732x1076+594+0 C:\Users\K017-Labor\Desktop\SetupFolder\Screenshots\A.jpg")
        os.system(r"magick C:\Users\K017-Labor\Desktop\SetupFolder\Screenshots\A.jpg -resize 50% C:\Users\K017-Labor\Desktop\SetupFolder\Saved_Pics\A.jpg")
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows() 