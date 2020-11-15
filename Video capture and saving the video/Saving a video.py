import cv2

cap = cv2.VideoCapture(0)

# To save a video, we write each frame in a file and give it fourcc code

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # We are setting all the four codes to XVID using the *
#           Parameters :   'filename', fourcc code, fps, resolution
vid_write = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))

while True:
    status, frame = cap.read()
    cv2.imshow("Video", frame)
    # Now we write the frame
    vid_write.write(frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break
cap.release()
cv2.destroyAllWindows()
