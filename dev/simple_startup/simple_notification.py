import time
import os
import platform

def send_alert():
    message = "This is an alert message for all terminal users."
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system(f'echo "{message}" | wall')

if __name__ == "__main__":
    while True:
        send_alert()
        time.sleep(5)  # Sleep for 60 seconds