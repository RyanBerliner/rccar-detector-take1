import cv2
import os

files = sorted(os.listdir('./all-images-detected'))
frames = []
size = None

for num, image in enumerate(files):
    full_image_name = f"./all-images-detected/{image}"
    img = cv2.imread(full_image_name)
    height, width, layers = img.shape
    if size is None:
        size = (width,height)
    print(f"add image to frames {num}, {full_image_name}")
    frames.append(img)

out = cv2.VideoWriter('detected-video-gopro.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20.0, size)

for num, frame in enumerate(frames):
    print(f"add image to frames {num}")
    out.write(frame)

out.release()
