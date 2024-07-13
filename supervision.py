INTERVAL = 5 # minutes
IMG_DIR = "/home/user/Pictures/Supervised/"
# Email configuration
SENDER = "user_name@gmail.com"   # Enter your gmail address
PASSWORD = "masked-16-digit-app-password"  # Enter your app password
RECIPIENTS = ["user_name1@gmail.com"]

import cv2
import os
import time
import argparse
from datetime import datetime, timedelta
from pynput import mouse, keyboard
import asyncio

####################### E-mail Toolkit ############################
import ssl
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.message import EmailMessage
from base64 import b64encode, b64decode
# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # For SSL
def ec(password):
    return b64encode(password.encode()).decode()
def dc(encrypted_password):
    return b64decode(encrypted_password.encode()).decode()
def send_mail(recipients, subject, body, attachment_path=None):
    port = SMTP_PORT
    sender_email = SENDER
    smtp_server = SMTP_SERVER
    password = PASSWORD

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = ", ".join(recipients)

    # Always use absolute path for `attachment_path`!!!
    if attachment_path and os.path.isfile(attachment_path):
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(attachment_path)}",
            )
            msg.add_attachment(
                part.get_payload(decode=True),
                maintype=part.get_content_maintype(),
                subtype=part.get_content_subtype(),
                filename=os.path.basename(attachment_path),
            )
    elif attachment_path is not None:
        print(f"Attachment path {attachment_path} is invalid!")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, dc(password))
        server.send_message(msg)
        print(f"Email has just been successfully sent to {', '.join(recipients)}")
##################################################################

# Parse arguments
parser = argparse.ArgumentParser(description="Mouse and keyboard activity monitoring script")
parser.add_argument('--keep', '-k', action='store_true', help="Keep the old files in the saving path")
parser.add_argument('--mail', '-m', action='store_true', help="Enable email sending")
args = parser.parse_args()

# Directory to save images
save_path = os.path.expanduser(IMG_DIR)
os.makedirs(save_path, exist_ok=True)

# Clear the directory if not keeping files
if not args.keep:
    for f in os.listdir(save_path):
        os.remove(os.path.join(save_path, f))

# Ignore initial input for 10 seconds
ignore_initial_input_duration = 10
ignore_until = datetime.now() + timedelta(seconds=ignore_initial_input_duration)

# Time duration to wait before next capture
capture_interval = timedelta(minutes=INTERVAL)
next_capture_time = datetime.now()
is_camera_locked = False # avoid conflicts while detecting simultaneous inputs

def on_input_detected():
    global is_camera_locked
    if(is_camera_locked):
        return
    global next_capture_time
    current_time = datetime.now()

    if current_time < ignore_until:
        return

    if current_time >= next_capture_time:
        capture_image()
        next_capture_time = current_time + capture_interval

def capture_image():
    global is_camera_locked
    is_camera_locked = True
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
        if args.mail:
            asyncio.run(send_image_email(file_path))
    else:
        print("Error: Could not capture image.")

    cap.release()
    is_camera_locked = False

async def send_image_email(image_path):
    subject = "Computer Is Accessed"
    body = f"Computer accessed. See attached image.\n\nImage captured at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    send_mail(RECIPIENTS, subject, body, image_path)


# Mouse Listeners
def on_click(x, y, button, pressed):
    on_input_detected()
def on_move(x, y):
    # pass: ignore moving of the mouse
    print(f"Mouse is moving to position ({x},{y}).")
def on_scroll(x, y, dx, dy):
    # pass: ignore scrolling of the mouse
    print(f"Mouse is scrolling to position ({x},{y}) with deltaX:{dx} and deltaY:{dy}.")

# Keyboard Listeners
def on_press(key):
    # pass: ignore press or release so it will not call function multiple times
    print("keyboard is pressed!")
def on_release(key):
    on_input_detected()

# Start the listeners
mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_release=on_release)

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
