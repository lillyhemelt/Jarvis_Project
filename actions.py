import os
import webbrowser
import psutil

def execute_task(command):
    command = command.lower()
    if "open website" in command:
        webbrowser.open("https://google.com")
        return "opening your browser now, ma'am"
    elif "shutdown" in command:
        os.system("shutdown /s /t 1")
        return "shutting down the system, ma'am"
    return "no system action found."