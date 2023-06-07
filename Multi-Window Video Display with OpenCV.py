# Managing Multiple Windows Size and Position in OpenCV
# This code demonstrates how to create and manage multiple windows with 
# different sizes and positions using OpenCV.

import cv2

# Import the necessary OpenCV library for image processing.

print(cv2.__version__)

# Display the OpenCV version.

# Constants for window configuration
rows = int(input('Boss, How Many Rows Do You Want? '))
columns = int(input('And How Many Columns Do You Want? '))
width = 1280
height = 720

# Set the desired number of rows, columns, and frame size.

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Create a VideoCapture object to capture video from the default camera.
# Set the properties of the VideoCapture object, including frame width, frame height, frames per second (FPS),
# and four character code (FOURCC) for video encoding.

while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame, (int(width / columns), int(height / columns)))

    # Read a frame from the camera and resize it to fit the specified number of columns.

    for i in range(0, rows):
        for j in range(0, columns):
            windName = 'Window' + str(i) + " x " + str(j)
            cv2.imshow(windName, frame)
            cv2.moveWindow(windName, int(width / columns) * j, int(height / columns + 30) * i)

    # Create multiple windows based on the specified number of rows and columns.
    # Display the resized frame in each window and move each window to its designated position.

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Break the loop if the 'q' key is pressed.

cam.release()

# Release the VideoCapture object.

cv2.destroyAllWindows()

# Close all windows.
