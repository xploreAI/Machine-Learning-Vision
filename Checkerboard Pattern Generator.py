# Title: "Checkerboard Pattern Generator"
# Explanation:
# - The code prompts the user to input the size of the board and the number of squares per row and column.
# - It then generates a checkerboard pattern using OpenCV by creating a frame and filling each square with alternating dark and light colors.
# - The color of each square is toggled using a conditional statement.
# - The pattern is displayed in real-time until the user presses 'q' to quit.
# - This project serves as a practice lesson for generating and visualizing patterns using OpenCV.

import cv2
import numpy as np

# Constants
board_size = int(input("What size of board do you want Boss?"))
num_squares = int(input('And sir, how many squares?'))
square_size = int(board_size / num_squares)

light_color = (0, 0, 255)  # Light color (red)
dark_color = (0, 0, 0)  # Dark color (black)
color = dark_color  # Initialize color as dark color

# Display the checkerboard pattern
while True:
    # Create the frame once outside the loop
    frame = np.zeros([board_size, board_size, 3], dtype=np.uint8)

    for row in range(0, num_squares):
        for col in range(0, num_squares):
            # Calculate the starting x and y positions of the current square
            frame[square_size * row: square_size * (row + 1), square_size * col: square_size * (col + 1)] = color

            # Toggle color between light and dark for each square
            if color == dark_color:
                color = light_color
            else:
                color = dark_color

        # Toggle color at the end of each row to ensure alternating pattern
        if color == dark_color:
            color = light_color
        else:
            color = dark_color

    cv2.imshow('Checkerboard', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cv2.destroyAllWindows()
