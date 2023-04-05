import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    cv2.imshow("Live Feed", frame)

    if(cv2.waitKey(1) & 0xFF == ord('c')):
        cv2.imwrite("/home/santo/Project/dataset/12.jpg", frame)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        cap.release()
        cv2.destroyAllWindows()