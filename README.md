         _    ____   ____ ___ ___ _____                   
        / \  / ___| / ___|_ _|_ _|_   _|___ _ __ _ __ __  
       / _ \ \___ \| |    | | | |  | |/ _ | '__| '_ ` _ \ 
      / ___ \ ___) | |___ | | | |  | |  __| |  | | | | | |
     /_/   \_|____/ \____|___|___| |_|\___|_|  |_| |_| |_|
              ASCIITerm - NDI Viewer for Terminals  

![ASCIITerm Screenshot](/ASCIITermHeader.png)

# Display NDI Video as ASCII Output in Terminal

## Description
`ASCIITerm.py` is a Python script for rendering video frames as ASCII art live in Terminal. 

This allows you to watch any movie or other recording in full, text-based glory.

This is designed to provide a "graphics" driver to old serial terminals for fun and profit. 

Inspired by [Modern Linux on a Wyse Terminal](https://www.youtube.com/watch?v=xQTr9ZOJkC0)

It uses OpenCV for image processing, NumPy for numerical operations, and NDIlib for network device interface capabilities.

## Setup

1. Install [NDI Tools](https://ndi.video/tools/) - this lets you pipe video around your system/network:
   
```
https://ndi.video/tools/
```

2. Clone this repo to your computer:
   
```
git clone https://github.com/mitchaiet/ASCIITerm.git
```

3. Install the required dependencies:
   
```
pip install -r requirements.txt
```
4. Run the script:
   
```
python3 ASCIITerm.py
```
## Settings

ASCIITerm defaults to a resolution of 80 columns, 24 rows.

Run the script with a custom column and row resolution to match your needs:
```
python3 ASCIITerm.py 100 30
```

## Usage

1. Create a new NDI Video Source. You can use the [NDI Tools Scan Converter](https://ndi.video/tools/ndi-scan-converter/) to select a window, like a video player, and render it to a new NDI Video Source.
   
3. Run the script with either the default (80x24) or custom resolution.
   
```
python3 ASCIITerm.py
```
or
```
python3 ASCIITerm.py 100 30
```

3. You will see the main source selection screen. Select a video source by typing a number:
   
```
                                                                                             
              _    ____   ____ ___ ___ _____                   
             / \  / ___| / ___|_ _|_ _|_   _|__ _ __ _ __ ___  
            / _ \ \___ \| |    | | | |  | |/ _ | '__| '_ ` _ \ 
           / ___ \ ___) | |___ | | | |  | |  __| |  | | | | | |
          /_/   \_|____/ \____|___|___| |_|\___|_|  |_| |_| |_|
                                                               
               ASCIITerm - NDI Viewer for Terminal Windows                                                                   
             
         Looking for sources...
         Available NDI sources:
         1: MACBOOK-PRO-8.LAN (NDI Virtual Input)
         2: MACBOOK-PRO-8.LAN (Scan Converter)
         Select a source (by number):
   ```


