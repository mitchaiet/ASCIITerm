
import subprocess
import cv2
import numpy as np
import os
import sys

ASCII_CHARS = "@%#*+=-:. "

def log(message):
    # Verbose logging function
    print(f"[LOG] {message}")

def frame_to_ascii(frame, cols=80, rows=24):
    # Convert frame to ASCII characters
    frame = cv2.resize(frame, (cols, rows))
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ascii_art = ""
    for row in grayscale:
        for pixel in row:
            ascii_art += ASCII_CHARS[pixel // 28]
        ascii_art += "\n"
    return ascii_art

def list_windows():
    # Use wmctrl to list windows. Requires 'wmctrl' to be installed on Ubuntu.
    log("Listing available windows...")
    try:
        output = subprocess.check_output(["wmctrl", "-l"]).decode()
        windows = output.splitlines()
        window_dict = {}
        for index, win in enumerate(windows, start=1):
            win_id = win.split()[0]
            window_dict[index] = win_id
            print(f"{index}: {win}")
        return window_dict
    except Exception as e:
        log(f"Error listing windows: {e}")
        sys.exit(1)

def select_window(window_dict):
    # Simple window selection by numerical ID
    while True:
        try:
            choice = int(input("Enter the ID of the window to capture: "))
            if choice in window_dict:
                return window_dict[choice]
            else:
                print("Invalid ID. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def get_window_geometry(window_id):
    # Use xwininfo to get the geometry of the window
    try:
        output = subprocess.check_output(["xwininfo", "-id", window_id]).decode()
        geometry = {}
        for line in output.splitlines():
            if "Absolute upper-left X:" in line:
                geometry["x"] = line.split(":")[1].strip()
            if "Absolute upper-left Y:" in line:
                geometry["y"] = line.split(":")[1].strip()
            if "Width:" in line:
                geometry["width"] = line.split(":")[1].strip()
            if "Height:" in line:
                geometry["height"] = line.split(":")[1].strip()
        return geometry
    except Exception as e:
        log(f"Error getting window geometry: {e}")
        sys.exit(1)

def capture_window(window_geometry):
    # Use FFMPEG to capture the selected window area.
    log(f"Capturing window at {window_geometry}...")
    command = [
        'ffmpeg',
        '-f', 'x11grab',
        '-video_size', f'{window_geometry["width"]}x{window_geometry["height"]}',
        '-i', f':0.0+{window_geometry["x"]},{window_geometry["y"]}',
        '-vf', 'scale=80:24',  # Adjust scale to match ASCII dimensions
        '-f', 'image2pipe',
        '-pix_fmt', 'rgb24',
        '-vcodec', 'rawvideo', '-'
    ]
    return subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=10**8)

def main():
    window_dict = list_windows()
    window_id = select_window(window_dict)
    window_geometry = get_window_geometry(window_id)
    ffmpeg_process = capture_window(window_geometry)

    try:
        while True:
            raw_frame = ffmpeg_process.stdout.read(80 * 24 * 3)  # Width * Height * RGB
            if not raw_frame:
                break

            frame = np.frombuffer(raw_frame, np.uint8).reshape((24, 80, 3))
            ascii_frame = frame_to_ascii(frame)
            print(ascii_frame)

            ffmpeg_process.stdout.flush()
    except KeyboardInterrupt:
        log("Stream interrupted by user.")

    finally:
        ffmpeg_process.terminate()
        log("FFMPEG process terminated.")

if __name__ == "__main__":
    main()
