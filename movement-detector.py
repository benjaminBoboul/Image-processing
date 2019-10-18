#!/usr/bin/env python
import cv2
import imutils

def save_webcam(mirror=False):
    cap = cv2.VideoCapture(0) # Capturing video from webcam:
    currentFrame = 0
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # Get current width of frame
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # Get current height of frame
    old = None

    while (cap.isOpened()): # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            if mirror == True: 
                # Mirror the output video frame
                frame = cv2.flip(frame, 1)
            # Saves for video
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if old is not None:
                if old.shape[:2] == frame.shape[:2]:
                    diff = cv2.absdiff(old, gray)
                    diff = cv2.threshold(diff, 5, 255, cv2.THRESH_BINARY)[1]
                    diff = cv2.medianBlur(diff, 55, 0)
                    if diff.mean() > 0.2:
                        print("Motion detected")
                    else:
                        print("Nothing is moving")
                    cnts = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    cnts = imutils.grab_contours(cnts)
                    for c in cnts:
                        # if the contour is too small, ignore it
                        if cv2.contourArea(c) < 500:
                            continue
                
                        # compute the bounding box for the contour, draw it on the frame,
                        # and update the text
                        (x, y, w, h) = cv2.boundingRect(c)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.imshow('frame_blurred', diff)
            cv2.imshow('frame', frame)
            old = gray
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'): # if 'q' is pressed thenquit
            break
        # To stop duplicate images
        currentFrame += 1
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def main():
    save_webcam(mirror=True)

if __name__ == '__main__':
    main()