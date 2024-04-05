import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

# Initializing camera and hand detector
cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 420)
detector = HandDetector(detectionCon=0.7, maxHands=1)
keyboard = Controller()

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        fingers = detector.fingersUp(hands[0])
        if fingers == [0, 0, 0, 0, 0]:
            keyboard.press(Key.left)
            keyboard.release(Key.right)
            keyboard.release(Key.up)
        elif fingers == [1, 1, 1, 1, 1]:
            keyboard.press(Key.right)
            keyboard.release(Key.up)
            keyboard.release(Key.left)
        elif fingers == [1, 1, 1, 0, 0]:
            keyboard.press(Key.up)
            keyboard.release(Key.left)
            keyboard.release(Key.right)
    else:
        keyboard.release(Key.left)
        keyboard.release(Key.right)
        keyboard.release(Key.up)
    cv2.imshow("Gesture-Controlled Hill Climb Racing", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()