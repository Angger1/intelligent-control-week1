import cv2
import numpy as np

def detect_color_and_draw_box_from_camera(lower_bound, upper_bound):
    cap = cv2.VideoCapture(0)  # Gunakan kamera default
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_bound, upper_bound)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        cv2.imshow("Detected Color", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Contoh penggunaan (deteksi warna merah)
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

detect_color_and_draw_box_from_camera(lower_red, upper_red)