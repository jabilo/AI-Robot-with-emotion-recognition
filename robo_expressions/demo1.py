import cv2

def play_expression(exp):
    
   
    # Open the video file
    cap = cv2.VideoCapture(exp)

    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error opening video file")

    # Play the video in a loop
    while True:
        # Read a frame from the video file
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            # If not, restart the video from the beginning
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # Display the frame
        cv2.imshow('Video', frame)

        # Wait for a key press and check if the 'q' key was pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video file and close the window
    cap.release()
    cv2.destroyAllWindows()


sad = 'robo_expressions\sad.mp4'
happy = 'robo_expressions\happy.mp4'
mad = 'robo_expressions\mad.mp4'
cute = 'robo_expressions\cute.mp4'
play_expression(happy)
play_expression(sad)