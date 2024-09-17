#================================================
# Title: Qrcode Reader
# Usage: python3 qrcode.py
#================================================
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import argparse

def main():

    #parsing arguments------------------------------
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=int, default = 0, help="camera source")
    args = parser.parse_args()

    # Initialize the webcam
    cap = cv2.VideoCapture(args.source)  # 0 is the ID of the default camera, change if multiple cameras are connected

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

   
    
    # Read frames from the webcam in a loop
    while True:
        ret, frame = cap.read()  # Capture frame-by-frame
        if not ret:
            print("Error: Failed to capture image.")
            break

        for barcode in decode(frame):
            myData = barcode.data.decode("utf-8")
            print(myData)
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (0,0,255), 5)
            pts2 = barcode.rect
            cv2.putText(frame, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)


        # Display the frame
        cv2.imshow('Webcam', frame)

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()
#========================================
if __name__=="__main__": main()