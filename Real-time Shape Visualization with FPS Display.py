# Explanation:
# -The code uses OpenCV to capture video frames from the default camera.
# -It sets the frame width, height, FPS, and codec for the video capture.
# -The program enters a while loop to continuously read frames from the camera.
# -Several shapes are drawn on each frame using OpenCV's drawing functions:
# -A filled rectangle is drawn in the center of the frame.
# -A circle is drawn around the rectangle.
# -A line is drawn from the top-left corner to the bottom-right corner.
# -A filled ellipse is drawn in the top-right corner.
# -The code calculates and displays the Frames Per Second (FPS) on the frame.
# -The modified frame is displayed using the cv2.imshow() function.
# -The loop continues until the user presses 'q' to quit.
# -Finally, the VideoCapture object is released, and all windows are closed.
# IN SUMMARY, This code generates a live video feed with dynamically drawn shapes and FPS information, 
# providing an interactive visual experience.

import cv2

# Constants
width = 640
height = 360

# Create VideoCapture object
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Variables for FPS calculation
start_time = cv2.getTickCount()
frame_counter = 0

while True:
    # Read frame from camera
    ret, frame = cam.read()
    
    # Draw a rectangle in the center of the frame
    rectangle_color = (0, 0, 255)
    rectangle_position = (int(width/2 - 50), int(height/2 - 50))
    rectangle_size = (100, 100)
    cv2.rectangle(frame, rectangle_position, (rectangle_position[0] + rectangle_size[0], rectangle_position[1] + rectangle_size[1]), rectangle_color, -1)
    
    # Draw a circle around the rectangle
    circle_color = (255, 0, 0)
    circle_center = (int(width/2), int(height/2))
    circle_radius = 120
    cv2.circle(frame, circle_center, circle_radius, circle_color, 3)
    
    # Draw a line from top-left to bottom-right
    line_color = (0, 255, 0)
    cv2.line(frame, (0, 0), (width, height), line_color, 2)
    
    # Draw an ellipse in the top-right corner
    ellipse_color = (0, 255, 255)
    ellipse_center = (int(width/2) + 100, 50)
    ellipse_axes = (100, 50)
    cv2.ellipse(frame, ellipse_center, ellipse_axes, 0, 0, 360, ellipse_color, -1)
    
    # Calculate and display FPS
    frame_counter += 1
    elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
    fps = frame_counter / elapsed_time
    cv2.putText(frame, "FPS: {:.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    # Display the frame
    cv2.imshow('OpenCV Shapes', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close windows
cam.release()
cv2.destroyAllWindows()
