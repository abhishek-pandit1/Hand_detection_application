# Hand Detection Login Application

This project is a Python application that combines a simple login GUI with real-time hand detection using OpenCV and MediaPipe. After a successful login, the application uses your webcam to detect and display information about the hands it sees.

## Features
- **Login Interface:** Simple Tkinter-based GUI for user authentication.
- **Hand Detection:** Uses MediaPipe and OpenCV to detect left, right, both, or multiple hands in real-time from your webcam.
- **Visual Feedback:** Displays detected hand type (left/right/both/multiple) on the video feed.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- MediaPipe
- Tkinter (usually included with Python)
- protobuf (for `google.protobuf.json_format`)

You can install the required packages using pip:
```bash
pip install opencv-python mediapipe protobuf
```

## Usage
1. **Run the script:**
   ```bash
   python tut3.py
   ```
2. **Login:**
   - Username: `admin`
   - Password: `password`
3. After successful login, your webcam will activate and start detecting hands.
4. Press `q` to quit the hand detection window.

## How it Works
- The application starts with a login window.
- On correct credentials, it opens the webcam and processes the video feed to detect hands using MediaPipe.
- It displays messages on the video feed indicating whether it sees a left hand, right hand, both hands, or multiple hands.

## Notes
- The login credentials are hardcoded for demonstration purposes.
- Make sure your webcam is connected and accessible.

## License
This project is for educational purposes. 
