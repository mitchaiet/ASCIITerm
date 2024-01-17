import sys
import numpy as np
import cv2 as cv
import NDIlib as ndi

ASCII_CHARS = "@%#*+=-:. "

# Global flag for verbose logging
verbose_logging = True

def log(message):
    if verbose_logging:
        print(message)

def frame_to_ascii(frame, cols=80, rows=24):
    frame = cv.resize(frame, (cols, rows))
    grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ascii_art = ""
    for row in grayscale:
        for pixel in row:
            ascii_art += ASCII_CHARS[pixel // 28]
        ascii_art += "\n"
    return ascii_art

def main(cols=80, rows=26):
    ascii_logo = """                                                                                    
     _    ____   ____ ___ ___ _____                   
    / \  / ___| / ___|_ _|_ _|_   _|__ _ __ _ __ ___  
   / _ \ \___ \| |    | | | |  | |/ _ | '__| '_ ` _ \ 
  / ___ \ ___) | |___ | | | |  | |  __| |  | | | | | |
 /_/   \_|____/ \____|___|___| |_|\___|_|  |_| |_| |_|
                                                      
      ASCIITerm - NDI Viewer for Terminal Windows                                                                   
    """
    print(ascii_logo)

    if not ndi.initialize():
        log("NDI failed to initialize.")
        return 0

    ndi_find = ndi.find_create_v2()
    if ndi_find is None:
        log("Failed to create NDI finder.")
        return 0

    log('Looking for sources...')
    ndi.find_wait_for_sources(ndi_find, 5000)
    sources = ndi.find_get_current_sources(ndi_find)

    if not sources:
        log('No sources found.')
        ndi.find_destroy(ndi_find)
        ndi.destroy()
        return 0

    log('Available NDI sources:')
    for i, source in enumerate(sources):
        log(f"{i + 1}: {source.ndi_name}")

    source_index = int(input("Select a source (by number): ")) - 1
    if source_index < 0 or source_index >= len(sources):
        log('Invalid source number.')
        ndi.find_destroy(ndi_find)
        ndi.destroy()
        return 0

    ndi_recv_create = ndi.RecvCreateV3()
    ndi_recv_create.color_format = ndi.RECV_COLOR_FORMAT_BGRX_BGRA
    ndi_recv = ndi.recv_create_v3(ndi_recv_create)
    if ndi_recv is None:
        log("Failed to create NDI receiver.")
        return 0

    ndi.recv_connect(ndi_recv, sources[source_index])
    ndi.find_destroy(ndi_find)

    while True:
        try:
            t, v, _, _ = ndi.recv_capture_v2(ndi_recv, 5000)
            if t == ndi.FRAME_TYPE_VIDEO:
                frame = np.copy(v.data)
                ascii_art = frame_to_ascii(frame, cols, rows)
                print(ascii_art)
                ndi.recv_free_video_v2(ndi_recv, v)
        except KeyboardInterrupt:
            break

    ndi.recv_destroy(ndi_recv)
    ndi.destroy()

    return 0

if __name__ == "__main__":
    cols = int(sys.argv[1]) if len(sys.argv) > 1 else 80
    rows = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    sys.exit(main(cols, rows))
