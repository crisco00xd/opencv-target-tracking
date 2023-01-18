import cv2


# Set the camera index (usually 0 for a built-in webcam, 1 for external webcam, etc.)
print(f'Setting Up Camera')
camera_index = 0

# Initialize the camera
cap = cv2.VideoCapture(camera_index)

# Set the desired width and height of the camera stream
print(f'Setting Up Camera Resolution')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Set the desired target color (in this case, blue)
target_color = (255, 0, 0)

# Set the camera's latitude and longitude (assuming it is stationary)
camera_latitude = 18.045338
camera_longitude = -67.167846

print(f'Starting While Loop')
while True:
    # Capture the current frame from the camera
    ret, frame = cap.read()

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of colors to detect (in this case, blue)
    lower_color = (100, 150, 0)
    upper_color = (140, 255, 255)

    # Create a mask for the target color
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Iterate over the contours and find the largest one
    target_contour = None
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            target_contour = contour

    # If a target was found, draw a rectangle around it and display the latitude and longitude
    if target_contour is not None:
        # Get the bounding box of the target
        x, y, w, h = cv2.boundingRect(target_contour)

        # Calculate the latitude and longitude of the target based on its position in the frame
        target_latitude = camera_latitude + (y - (frame.shape[0] / 2)) * 0.00001
        target_longitude = camera_longitude + (x - (frame.shape[1] / 2)) * 0.00001

        # Draw the rectangle around the target
        cv2.rectangle(frame, (x, y), (x + w, y + h), target_color, 2)

        # Put the latitude and longitude on the frame
        cv2.putText(frame, f"Lat: {target_latitude:.6f}, Long: {target_longitude:.6f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, target_color, 2)

    # Display the image
    cv2.imshow("Camera Stream", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
