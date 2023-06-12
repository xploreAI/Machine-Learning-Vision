"""
ROI Selection and Capture from Webcam

This script allows the user to select regions of interest (ROI) from the webcam feed and capture/save them as image files.

Usage:
- Press 'r' to reset and clear the current ROI selection.

Controls:
- Left-click and drag to draw a rectangle or shape.
- Middle-click to select a circle shape.
"""

import cv2
import os
from datetime import datetime
import numpy as np

# Global variables
evt = 0
pnt1 = ()
pnt2 = ()
shape_type = ""
tooltip = ""

# Define initial ROI variable
ROI = None

def mouseClick(event, xPos, yPos, flags, params):
    """
    Mouse click event handler function.

    Args:
    - event: Mouse event type
    - xPos: x-coordinate of the mouse cursor
    - yPos: y-coordinate of the mouse cursor
    - flags: Additional flags
    - params: Additional parameters

    Returns: None
    """
    global pnt1
    global evt
    global pnt2
    global shape_type
    global tooltip

    if event == cv2.EVENT_LBUTTONDOWN:
        pnt1 = (xPos, yPos)
        evt = event
    elif event == cv2.EVENT_LBUTTONUP:
        pnt2 = (xPos, yPos)
        evt = event
    elif event == cv2.EVENT_RBUTTONUP:
        evt = event

    if event == cv2.EVENT_MBUTTONDOWN:
        shape_type = "circle"
        tooltip = "Shape: Circle"

# Set up webcam properties
width = 640
height = 360

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Create a named window for the webcam feed
cv2.namedWindow('My Webcam')
cv2.setMouseCallback('My Webcam', mouseClick)

# Create an output directory for saving ROIs
output_directory = 'ROI_Captures'
os.makedirs(output_directory, exist_ok=True)

while True:
    # Read a frame from the webcam
    ret, frame = cam.read()
    # Check if the frame was successfully captured
    if not ret:
        print("Failed to capture frame from webcam.")
        break

    # Display tooltip/help message on the frame
    if tooltip:
        cv2.putText(frame, tooltip, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    if evt == 4:
        # Check the selected shape type
        # Draw a rectangle on the frame
        cv2.rectangle(frame, pnt1, pnt2, (221, 124, 126), 2)
        # Extract the ROI using the rectangle coordinates
        ROI = frame[pnt1[1]:pnt2[1], pnt1[0]:pnt2[0]]
        if shape_type == "circle":
            # Calculate the radius of the circle
            radius = int(np.sqrt((pnt2[0] - pnt1[0]) ** 2 + (pnt2[1] - pnt1[1]) ** 2))
            # Draw a circle on the frame
            cv2.circle(frame, pnt1, radius, (221, 124, 126), 2)
            # Create a mask for the circle
            mask = np.zeros(frame.shape[:2], dtype=np.uint8)
            cv2.circle(mask, pnt1, radius, 255, -1)
            # Apply the mask to extract the ROI
            ROI = cv2.bitwise_and(frame, frame, mask=mask)

        # Display the ROI in a separate window
        if ROI is not None:
            cv2.imshow('ROI', ROI)
            cv2.moveWindow('ROI', int(width * 1.1), 0)

    # Capture and save the ROI
    if evt == 5:
        cv2.destroyWindow('ROI')
        if ROI is not None:
            # Generate a unique filename based on current timestamp
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
            filename = os.path.join(output_directory, f'ROI_{shape_type}_{timestamp}.png')
            cv2.imwrite(filename, ROI)
            print(f'ROI saved as {filename}')

        # Reset variables and tooltip
        evt = 0
        shape_type = ""
        tooltip = ""

    # Display the webcam frame
    cv2.imshow('My Webcam', frame)
    cv2.moveWindow('My Webcam', 0, 0)

    # Check for keypress events
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('r'):
        tooltip = "Action: Reset"
        evt = 5  # Simulate right button up event to reset ROI

# Release the webcam and destroy windows
cam.release()
cv2.destroyAllWindows()
