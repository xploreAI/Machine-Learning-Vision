# Title: "Real-Time Color and Gray Frame Display"

# Explanation:
# This code utilizes OpenCV to display real-time color and grayscale frames captured from a camera. 
# It sets the desired width, height, and frames per second (FPS) for the video capture. 
# Inside the loop, it reads frames from the camera and converts them to grayscale using the cv2.cvtColor() function. 
# The color and grayscale frames are displayed in separate windows using cv2.imshow(). The cv2.moveWindow() function 
# is used to set the position of each window. The loop continues until the user presses the 'q' key. 
# Finally, the camera is released and the windows are closed.

import cv2

# Print OpenCV version
print(cv2.__version__)

# Set the desired width and height for the video capture
width = 480
height = 240

# Create VideoCapture object
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    # Read frame from camera
    ignore, frame = cam.read()

    # Convert frame to grayscale
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display color frame
    cv2.imshow('Color Frame', frame)
    cv2.moveWindow('Color Frame', 0, 0)

    # Display grayscale frame
    cv2.imshow('Gray Frame', grayframe)
    cv2.moveWindow('Gray Frame', 420, 0)

    # Display color frame 2
    cv2.imshow('Color Frame 2', frame)
    cv2.moveWindow('Color Frame 2', 420, 270)

    # Display grayscale frame 2
    cv2.imshow('Gray Frame 2', grayframe)
    cv2.moveWindow('Gray Frame 2', 0, 270)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close windows
cam.release()
cv2.destroyAllWindows()
