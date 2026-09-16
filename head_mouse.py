import cv2
import pyautogui

pyautogui.FAILSAFE = False

cam = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

screen_w, screen_h = pyautogui.size()

while True:

    ret, frame = cam.read()

    if not ret:
        print("Camera is not providing an image.")
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(80, 80)
    )

    for (x, y, w, h) in faces:

        center_x = x + w // 2
        center_y = y + h // 2

        frame_w = frame.shape[1]
        frame_h = frame.shape[0]

        mouse_x = int(
            center_x / frame_w * screen_w
        )

        mouse_y = int(
            center_y / frame_h * screen_h
        )

        mouse_x = max(
            10,
            min(mouse_x, screen_w - 10)
        )

        mouse_y = max(
            10,
            min(mouse_y, screen_h - 10)
        )

        pyautogui.moveTo(
            mouse_x,
            mouse_y,
            duration=0.01
        )

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.circle(
            frame,
            (center_x, center_y),
            5,
            (0, 0, 255),
            -1
        )

    cv2.imshow(
        "Head Mouse",
        frame
    )

    key = cv2.waitKey(10) & 0xFF

    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
