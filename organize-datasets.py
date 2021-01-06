import os, os.path, glob
import random
import math
import shutil

has_run = len(os.listdir('./datasets/train/images')) > 0 or len(os.listdir('./datasets/validation/images')) > 0

if has_run:
    print('Already organized datasets, exiting.')
    exit()

images = []
os.chdir('./datasets/all/')
for image in glob.glob("*.jpg"):
    images.append(image)

random.shuffle(images)
num_images = len(images)
training_size = math.ceil(num_images * .75)  # train with 75% of the available data

os.chdir('../')

for i, image in enumerate(images):
    number = image[:-4]
    image_path = f"./all/{image}"
    annotation_path = f"./all/{number}.xml"
    if i <= training_size:
        image_dest = f"./train/images/{image}"
        annotation_dest = f"./train/annotations/{number}.xml"
    else:
        image_dest = f"./validation/images/{image}"
        annotation_dest = f"./validation/annotations/{number}.xml"
    print(f"copying {image_path} to {image_dest}")
    shutil.copy(image_path, image_dest)
    print(f"copying {annotation_path} to {annotation_dest}")
    shutil.copy(annotation_path, annotation_dest)
