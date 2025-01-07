import cv2
from PIL import Image

from util import get_limits


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV color space
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Loop over the colors to detect: red, green, blue
    for color in ['red', 'green', 'blue']:
        # Get the color limits from get_limits
        if color == 'red':
            lowerLimit1, upperLimit1 = get_limits(color)[0]
            lowerLimit2, upperLimit2 = get_limits(color)[1]
            # Create masks for both red ranges
            mask1 = cv2.inRange(hsvImage, lowerLimit1, upperLimit1)
            mask2 = cv2.inRange(hsvImage, lowerLimit2, upperLimit2)
            # Combine the two red masks
            mask = cv2.bitwise_or(mask1, mask2)
        else:
            lowerLimit, upperLimit = get_limits(color)
            # Create the mask for the color
            mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Loop through each contour
        for contour in contours:
            if cv2.contourArea(contour) > 1000:  # Only process contours with area > 1000
                # Get the bounding box of the contour
                x, y, w, h = cv2.boundingRect(contour)

                # Draw bounding boxes around the detected color
                if color == 'red':
                    color_bgr = (0, 0, 255)  # Red in BGR format
                elif color == 'green':
                    color_bgr = (0, 255, 0)  # Green in BGR format
                elif color == 'blue':
                    color_bgr = (255, 0, 0)  # Blue in BGR format

                # Draw a rectangle around the detected region
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), color_bgr, 5)

    # Show the processed frame with bounding boxes
    cv2.imshow('frame', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
