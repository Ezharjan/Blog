# pip install pynput opencv-python-headless
import cv2
import os
import time
from datetime import datetime, timedelta
from pynput import mouse, keyboard

INTERVAL = 0.1 # minutes

# Directory to save images
save_path = os.path.expanduser("~/Pictures/Supervised/")
os.makedirs(save_path, exist_ok=True)

# Flag to determine if we should keep old files
import sys
keep_files = '--keep' in sys.argv or '-k' in sys.argv

# Clear the directory if not keeping files
if not keep_files:
    for f in os.listdir(save_path):
        os.remove(os.path.join(save_path, f))

# Ignore initial input for 10 seconds
ignore_initial_input_duration = 10
ignore_until = datetime.now() + timedelta(seconds=ignore_initial_input_duration)

# Time duration to wait before next capture
capture_interval = timedelta(minutes=INTERVAL)
next_capture_time = datetime.now()

def on_input_detected():
    global next_capture_time
    current_time = datetime.now()

    if current_time < ignore_until:
        return

    if current_time >= next_capture_time:
        capture_image()
        next_capture_time = current_time + capture_interval

def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    ret, frame = cap.read()
    if ret:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(save_path, f"capture_{timestamp}.png")
        cv2.imwrite(file_path, frame)
        print(f"Image captured and saved to {file_path}")
    else:
        print("Error: Could not capture image.")

    cap.release()

# Mouse and keyboard listeners
def on_move(x, y):
    on_input_detected()

def on_click(x, y, button, pressed):
    on_input_detected()

def on_scroll(x, y, dx, dy):
    on_input_detected()

def on_press(key):
    on_input_detected()

def on_release(key):
    on_input_detected()

# Start the listeners
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)

mouse_listener.start()
keyboard_listener.start()

# Keep the script running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Script terminated by user.")

mouse_listener.stop()
keyboard_listener.stop()

