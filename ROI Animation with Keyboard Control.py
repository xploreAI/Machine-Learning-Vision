"""
Title: ROI Animation with Keyboard Control

This Python script captures video from the default camera and displays it in a window. 
It allows you to control a Region of Interest (ROI) within the frame using keyboard inputs. 
The ROI can be resized, moved, and the direction of its movement can be changed.

Keyboard Controls:
- 'i': Increase ROI size
- 'd': Decrease ROI size
- 'm': Change movement direction
- 'p': Pause/resume animation
- 'q': Quit the program

"""

import cv2

# Set the dimensions of the frame and the ROI snippet
width = 640
height = 360
snipW = 200
snipH = 80

# Initialize the starting position of the ROI box
boxCR = int(height/2)
boxCC = int(width/2)

# Set the direction and speed of the ROI box movement
deltaRow = 1
deltaCol = 1

roiSizeChange = 10
movementSpeed = 5
isPaused = False

# Create a VideoCapture object to capture video from the default camera
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Keyboard event handler function
def onKeyPress(event):
    global snipW, snipH, movementSpeed, isPaused, deltaRow, deltaCol

    # Increase ROI size
    if event == ord('i'):
        snipW += roiSizeChange
        snipH += roiSizeChange

    # Decrease ROI size
    elif event == ord('d'):
        if snipW > roiSizeChange and snipH > roiSizeChange:
            snipW -= roiSizeChange
            snipH -= roiSizeChange

    # Change movement direction
    elif event == ord('m'):
        deltaRow *= -1
        deltaCol *= -1

    # Pause/resume animation
    elif event == ord('p'):
        isPaused = not isPaused

# Create named windows for displaying the frames
cv2.namedWindow('My ROI')
cv2.namedWindow('My WEBcam')

# Variables for FPS calculation
start_time = cv2.getTickCount()
frame_counter = 0

while True:
    # Read a frame from the video capture
    ret, frame = cam.read()

    # Extract the ROI from the frame
    frameROI = frame[int(boxCR-snipH/2):int(boxCR+snipH/2), int(boxCC-snipW/2):int(boxCC+snipW/2)]

    # Convert the frame to grayscale and then back to BGR color format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    # Update ROI position based on movement speed and direction
    if not isPaused:
        if boxCR - snipH/2 <= 0 or boxCR + snipH/2 >= height:
            deltaRow *= -1
        if boxCC - snipW/2 <= 0 or boxCC + snipW >= width:
            deltaCol *= -1

        boxCR += deltaRow * movementSpeed
        boxCC += deltaCol * movementSpeed

    # Place the ROI back onto the frame
    frame[int(boxCR-snipH/2):int(boxCR+snipH/2), int(boxCC-snipW/2):int(boxCC+snipW/2)] = frameROI

    # Add graphical overlays
    cv2.rectangle(frame, (int(boxCC-snipW/2), int(boxCR-snipH/2)), (int(boxCC+snipW/2), int(boxCR+snipH/2)), (125, 255, 200), 2)
    cv2.putText(frame, f"ROI: ({snipW}x{snipH})", (10, height-20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.putText(frame, "Press 'q' to exit", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Calculate and display FPS
    frame_counter += 1
    elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
    fps = frame_counter / elapsed_time
    cv2.putText(frame, "FPS: {:.2f}".format(fps), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Display the ROI and the frame with the ROI
    cv2.imshow('My ROI', frameROI)
    cv2.moveWindow('My ROI', width, 0)
    cv2.imshow('My WEBcam', frame)
    cv2.moveWindow('My WEBcam', 0, 0)

    # Wait for a keyboard event and handle it
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    onKeyPress(key)

# Release the video capture and close windows
cam.release()
cv2.destroyAllWindows()
