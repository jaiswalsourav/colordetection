import cv2
from PIL import Image

# Define the get_limits function to return HSV color ranges
def get_limits(color):
    if color == 'red':
        # Red has two ranges in HSV space (red wraps around)
        lowerLimit1 = (0, 120, 70)  # Lower range for red
        upperLimit1 = (10, 255, 255)  # Upper range for red
        lowerLimit2 = (170, 120, 70)  # Lower range for red on the other side of hue spectrum
        upperLimit2 = (180, 255, 255)  # Upper range for red
        return [(lowerLimit1, upperLimit1), (lowerLimit2, upperLimit2)]
    
    elif color == 'green':
        # Green color range in HSV
        lowerLimit = (35, 50, 50)  # Lower limit for green
        upperLimit = (85, 255, 255)  # Upper limit for green
        return (lowerLimit, upperLimit)
    
    elif color == 'blue':
        # Blue color range in HSV
        lowerLimit = (100, 150, 0)  # Lower limit for blue
        upperLimit = (140, 255, 255)  # Upper limit for blue
        return (lowerLimit, upperLimit)
