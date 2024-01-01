         _    ____   ____ ___ ___ _____                   
        / \  / ___| / ___|_ _|_ _|_   _|___ _ __ _ __ __  
       / _ \ \___ \| |    | | | |  | |/ _ | '__| '_ ` _ \ 
      / ___ \ ___) | |___ | | | |  | |  __| |  | | | | | |
     /_/   \_|____/ \____|___|___| |_|\___|_|  |_| |_| |_|
         ASCIITerm - NDI Viewer for Terminal Windows  
Display NDI Video as ASCII Output in Terminal

![ASCIITerm Screenshot](/ASCIITermHeader.png)

## Description
`ASCIITerm.py` is a Python script for rendering video frames as ASCII art live in Terminal. 

This allows you to watch any movie or other recording in full, text-based glory.

This is designed to provide a "graphics" driver to old serial terminals for fun and profit. 

Inspired by [Modern Linux on a Wyse Terminal](https://www.youtube.com/watch?v=xQTr9ZOJkC0)

It uses OpenCV for image processing, NumPy for numerical operations, and NDIlib for network device interface capabilities.

## Setup

1. Install [NDI Tools](https://ndi.video/tools/) - this lets you pipe video around your system/network

2. Clone this repo to your computer

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the script:
   ```
   python ASCIITerm.py
   ```

ASCIITerm defaults to a resolution of 80 columns, 24 rows.
Run the script with a custom column and row resolution to match your needs:
   ```
   python ASCIITerm.py 100 30
   ```

## Usage

