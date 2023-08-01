import cv2
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter window
root = tk.Tk()
root.withdraw()

# Ask the user to select a video file
file_path = filedialog.askopenfilename()

# Open the video file
cap = cv2.VideoCapture(file_path)

# Check if the video file is successfully opened
if not cap.isOpened():
    print("Error opening the video file.")
    exit()

# Define lower and upper thresholds for fire color (red-orange)
lower_threshold = (0, 100, 100)
upper_threshold = (20, 255, 255)

# Iterate over each frame of the video
while True:
    # Read the current frame
    ret, frame = cap.read()

    # If the frame reading is unsuccessful, exit the loop
    if not ret:
        break

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask using the thresholds
    mask = cv2.inRange(hsv, lower_threshold, upper_threshold)

    # Apply morphological operations to enhance the mask
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Find contours of potential fire regions
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Process each contour
    fire_detected = False
    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)

        # If the area is smaller than a certain threshold, ignore it
        min_area = 1000  # Adjust this value based on your requirements
        if area < min_area:
            continue

        # Draw a bounding rectangle around the contour (green color)
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Draw another bounding rectangle to indicate fire detection (red color)
        cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 255), 50)

        # Set fire_detected flag to True
        fire_detected = True
        break  # Exit the loop if fire is detected

    # Display the frame with detected fire regions
    cv2.imshow('Fire Detection', frame)
    if fire_detected:
        print("Fire detected! Take immediate action.")
    else:
        print("No fire detected.")
    # Check if the 'q' key is pressed to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video file and close all windows
cap.release()
cv2.destroyAllWindows()
