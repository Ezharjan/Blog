import cv2
import os
import time
from datetime import datetime, timedelta
from pynput import mouse, keyboard
import smtplib
from base64 import b64encode, b64decode

INTERVAL = 0.1 # minutes
IMG_DIR = "~/Pictures/Supervised/"
# Email configuration
SENDER = "username@gmail.com"
PASSWORD = "xsadsadasdwkjeqiuycgi=="
RECIPIENT = "xxx@gmail.com"

#############################################################################################################
def ec(password):
    return b64encode(password.encode()).decode()

def dc(encrypted_password):
    return b64decode(encrypted_password.encode()).decode()

def send_email(recipients, content, subject="", sender=SENDER, pd=PASSWORD):
    message = f"Subject: {subject}\nFrom: {sender}\nTo: {', '.join(recipients)}\n\n{content}"
    with smtplib.SMTP('smtp.sina.com', 587) as smtp: # 587==>port4SMTP
        smtp.starttls()
        smtp.login(sender, dc(pd))
        smtp.sendmail(sender, recipients, message)
        print(f"Email sent to {', '.join(recipients)}")

# Directory to save images
save_path = os.path.expanduser(IMG_DIR)
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
        send_image_email(file_path)
    else:
        print("Error: Could not capture image.")

    cap.release()

def send_image_email(image_path):
    with open(image_path, "rb") as img_file:
        img_data = img_file.read()
    content = f"Computer accessed. See attached image.\n\n"
    content += f"Image captured at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    encoded_image = b64encode(img_data).decode('utf-8')
    content += f"\n\nAttachment:\n{encoded_image}"
    send_email([RECIPIENT], content, "Computer Is Accessed")

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

