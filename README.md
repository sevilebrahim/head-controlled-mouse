# Head-Controlled Mouse 🖱️

What if you could move the mouse without touching it?

That is the idea behind this project.

The program uses a webcam to detect a face in real time and finds the center of the detected face. That position is then mapped to the size of the computer screen, allowing the mouse cursor to follow the movement of the user's head.

As the face moves in front of the camera, the cursor moves in the same general direction. The camera window also shows the detected face with a rectangle and marks its center point.

This project combines computer vision with basic desktop automation and was a fun way to see how information from a camera can be turned into an action on the computer.

### The Idea Behind It

The process is simple:

```text
Webcam
   ↓
Face Detection
   ↓
Find Face Center
   ↓
Map Camera Position to Screen
   ↓
Move Mouse Cursor
```

The face is detected using OpenCV's Haar Cascade classifier, while PyAutoGUI is used to control the mouse.

### Technologies

* Python
* OpenCV
* PyAutoGUI

### What the Program Does

When the program starts, the webcam captures live video.

For every detected face, the program:

* Finds the center of the face
* Converts that position into screen coordinates
* Moves the mouse cursor to the corresponding location
* Displays the detected face and center point on the camera feed

Press **Q** to stop the program.

### Running the Project

Install the required libraries:

```bash
pip install opencv-python pyautogui
```

Then run:

```bash
python head_mouse.py
```

Make sure your webcam is available before starting the program.

### What I Learned

This project helped me connect two different areas of Python: computer vision and desktop automation.

Instead of only detecting something in a camera frame, I used the detected information to control another part of the computer in real time.

It was a useful exercise in working with coordinates, image dimensions, screen dimensions, webcam input, and real-time processing.

### Future Ideas

This project could be expanded by adding smoother cursor movement, gesture-based clicking, eye-blink detection, or other hands-free controls.
