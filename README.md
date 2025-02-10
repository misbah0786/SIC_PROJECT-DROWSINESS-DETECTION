# Drowsiness Detection System

This is a Tkinter-based GUI application that detects drowsiness using OpenCV, dlib, and Pygame for sound alerts. The application monitors eye landmarks to determine if a person is drowsy and raises an alarm if necessary.

## Features
- Real-time face and eye detection using dlib and OpenCV
- Alerts when drowsiness is detected
- Tkinter-based GUI with a simple interface
- Plays an alarm sound when drowsiness is detected
- Uses pygame.mixer for sound alerts

## Installation

### Prerequisites
Make sure you have Python 3.6+ installed on your system.

### Install Required Libraries
Run the following command to install the dependencies:

```sh
pip install opencv-python dlib pygame imutils tkinter
```

## Usage
1. Run the Script
```sh
python drowsiness_detection.py
```
2. Click the "Detect" button to start the drowsiness detection.
3. If drowsiness is detected, a red alert message will appear, and an alarm sound will play.
4. Press "Esc" to exit the detection.

## Folder Structure
```
/drowsiness-detection
│── facial-landmarks-recognition
│   ├── shape_predictor_68_face_landmarks.dat  # Pre-trained dlib model
│── alarm.mp3  # Alarm sound file
│── drowsiness_detection.py  # Main script
│── README.md  # This file
```

## Troubleshooting

### 1. "shape_predictor_68_face_landmarks.dat" file missing?
Download it from dlib's official dataset and place it in the `facial-landmarks-recognition/` folder.

### 2. Camera not opening?
- Check if your webcam is properly connected.
- Try changing the camera index in `cv2.VideoCapture(0)` (e.g., `cv2.VideoCapture(1)`).

### 3. No sound when drowsiness is detected?
- Ensure that `alarm.mp3` is in the same folder as the script.
- Install pygame using `pip install pygame`.

## License
This project is open-source and available under the MIT License.
