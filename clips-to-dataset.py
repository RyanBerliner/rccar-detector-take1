import numpy as np
import cv2
import math

DESIRED_HEIGHT = 1000

vids = [
  ('footage/gopro/clip1.mp4',),
  ('footage/iphone/clip1.MOV',),
  ('footage/gopro/clip2.mp4',),
  ('footage/iphone/clip2.MOV',),
  ('footage/gopro/clip3.mp4',),
  ('footage/iphone/clip3.MOV',),
]

image_number = 0

for vid in vids:
  cap = cv2.VideoCapture(vid[0])

  frame_count = 0

  while(cap.isOpened() and frame_count < 500):
      ret, frame = cap.read()
      frame_count += 1

      if frame is not None:
        image_number += 1
        shape = frame.shape

        og_height = shape[0]
        og_width = shape[1]

        # calculate ratio based on desired height and set new dimensions
        ratio = og_height / DESIRED_HEIGHT
        new_width = math.ceil(og_width / ratio)
        new_height = DESIRED_HEIGHT

        resized_frame = cv2.resize(frame, (new_width, new_height,))
        image_name = f"datasets/all/{image_number}.jpg"

        print(f"Saving vid {vid[0]} image {image_name}")
        cv2.imwrite(image_name, resized_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()