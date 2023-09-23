import cv2
import os
import re


image_folder = input("Please give the full path of the folder: ")
video_name = input("Please suggest a name of the final video file: ")

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]


def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [
        int(text)
        if text.isdigit() else text.lower()
        for text in _nsre.split(s)]

sorted_images = sorted(images, key=natural_sort_key)

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'MP4V'), 1, (width,height))

for image in sorted_images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
