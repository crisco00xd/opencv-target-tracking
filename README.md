# Color Detection using OpenCV
This code uses OpenCV, a popular computer vision library, to capture a video stream from a camera and detect a specific color (blue) within the frames. The code also calculates the latitude and longitude of the target based on its position in the frame, and displays it on the video stream.

## How to run
1. Install OpenCV by running ```pip install opencv-python``` on the command line.
2. Set the camera index to match your device camera. The default camera index is 0, but you may need to change it if you're using an external webcam.
3. Run the script using python.

## How it works
1. The code uses the ```cv2.VideoCapture()``` function to initialize the camera, and sets the desired width and height of the camera stream using ```cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)``` and ```cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)```.
2. The code then enters a while loop to continuously capture frames from the camera, convert them to the HSV color space, create a mask for the target color (blue), find contours in the mask, and iterate over the contours to find the largest one.
3. The code then calculates the latitude and longitude of the target based on its position in the frame, and displays it on the video stream with a rectangle drawn around it.

## Note: This code is for educational purposes only. The latitude and longitude calculation is not accurate as it is based on a simple formula derived from the center of the frame.
