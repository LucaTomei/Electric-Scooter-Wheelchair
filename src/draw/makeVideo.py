

import cv2
import os

image_folder = "/Users/lucasmac/Documents/Università/Magistrale/CS-Notes.nosync/Tesi/Tesi/Electric-Scooter-Wheelchair/src/draw/output/ES"
video_name = "ES.avi"

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images = sorted(images,key=lambda x: int(os.path.splitext(x)[0]))
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name,cv2.VideoWriter_fourcc(*'DIVX'), 15, (width, height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
