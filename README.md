# Fire Detection using OpenCV and tkinter

This Python script uses OpenCV to detect fire in a video. It identifies potential fire regions in the video frames and draws bounding rectangles around them. The script uses a simple colour-based approach to detect the fire's red-orange colour in the video frames.

## Table of Contents
- [Introduction](#introduction)
- [Instructions](#instructions)
- [Code Explanation](#code-explanation)
- [Important Note](#important-note)
- [Getting Started](#getting-started)
- [Technologies Used](#technologies-used)
- [Libraries Used](#libraries-used)
- [Code Usage Example](#code-usage-example)
- [License](#license)

## Introduction

Fire detection is crucial for early warning and effective firefighting. This Python script leverages the power of OpenCV, a popular computer vision library, to automatically detect fire in video footage. By analyzing colour and shape characteristics, the script can identify regions in the video that exhibit red-orange hues and approximate the presence of fire.

## Instructions

1. **Requirements**: Make sure you have Python and OpenCV installed on your system. You can install OpenCV using pip:

```bash
pip install opencv-python
```

2. **Download and Run**: Clone or download this repository to your local machine. Then, run the script "fire_detection.py".

3. **Select Video**: When prompted, use the file dialogue window to select a video file that you want to analyze for fire detection.

4. **Fire Detection Process**: The script will process each frame of the video and identify potential fire regions based on color characteristics.

5. **Output**: The script will display the video frames with bounding rectangles drawn around detected fire regions. If fire is detected in any frame, the script will print a message to take immediate action.

**Note**: To fine-tune the fire detection sensitivity, you can adjust the `min_area` value in the script.
![Screenshot 2023-08-14 180917](https://github.com/yesiamrajeev/Fire-Detection/assets/125568812/fe556814-8a72-4a31-9146-41c396ad1925)
![Screenshot 2023-08-14 180851](https://github.com/yesiamrajeev/Fire-Detection/assets/125568812/fb0a18ab-c66f-4b58-b9d7-539c84b82225)

# Code Explanation

The fire detection process involves the following steps:

1. **Video Input**: The script uses the OpenCV library to read a video file selected by the user.

2. **Color Filtering**: To identify potential fire regions, the script converts each frame to the HSV color space and applies color filtering within a predefined range for red-orange hues.

3. **Morphological Operations**: To reduce noise and improve accuracy, morphological operations, such as opening, are applied to the mask.

4. **Contour Detection**: The script identifies contours in the mask that may correspond to fire regions.

5. **Bounding Rectangles**: For each detected contour, the script draws a bounding rectangle around it to highlight the potential fire region.

6. **Fire Detection Indication**: Additionally, the script overlays a large red rectangle across the top of the frame to indicate fire detection visually.

## Important Note

- This script is intended for basic fire detection and should not be used as a primary safety measure. It is recommended to deploy specialized fire detection systems for critical applications.
- The accuracy of fire detection may vary depending on factors such as lighting conditions, video quality, and the presence of similar red-orange objects in the scene.
- The `min_area` parameter affects the sensitivity of fire detection. Smaller values may detect smaller fires but may also lead to false positives.

## Getting Started

To run the fire detection script, you need to have Python and OpenCV installed on your system. If you haven't installed OpenCV, you can do so using pip:

```bash
pip install opencv-python
```

After installing the required dependencies, clone or download this repository to your local machine, and then run the script as explained in the "Instructions" section.

## Technologies Used

- Python
- OpenCV

## Libraries Used

- OpenCV (cv2): Used for video input, color filtering, contour detection, and image processing operations.

## Code Usage Example

```bash
python fire_detection.py
```

Upon running the script, a file dialog will prompt you to select a video file. Choose the desired video, and the script will start processing the frames. The output window will display the video frames with any detected fire regions highlighted. If the script detects fire in any frame, it will print a message to take immediate action.

## License

This project is licensed under the [MIT License](LICENSE).
