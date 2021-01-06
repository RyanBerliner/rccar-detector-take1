from flask import Flask, render_template, request, abort, redirect, send_from_directory
from xml.dom import minidom 
import os
import random
import cv2


app = Flask(__name__)

@app.route('/datasets/<path:path>', methods=['GET'])
def get_datasets(path):
    return send_from_directory(f"{os.getcwd()}/../datasets", path)

@app.route('/', methods=['GET', 'POST'])
def annotator():
    images = os.listdir('../datasets/all/')
    num_images = len(images)
    image = request.values.get('image')

    if image is None or int(image) > num_images or image == '0':
        return redirect(f"/?image={1}")

    if request.method == 'GET':
        return render_template('index.html', image=image)
    elif request.method == 'POST':
        top_left_x = request.values.get('top_left_x')
        top_left_y = request.values.get('top_left_y')
        bottom_right_x = request.values.get('bottom_right_x')
        bottom_right_y = request.values.get('bottom_right_y')

        # if the form was partially filled out, have the person do the image again
        if '' in [top_left_x, top_left_y, bottom_right_x, bottom_right_y] \
            and (top_left_x == top_left_y == bottom_right_x == bottom_right_y) == False:
            return redirect(f"/?image={image}", code=302)

        im = cv2.imread(f"../datasets/all/{image}.jpg")
        h, w, c = im.shape

        rccarobjects = []
        if top_left_x != '':
            rccarobjects = [{
                'name': 'rccar',
                'pose': 'Unspecified',  # not dealing with this... 1 step at a time
                'truncated': 1 if request.values.get('truncated') else 0,
                'difficult': 1 if request.values.get('difficult') else 0,
                'xmin': top_left_x,
                'ymin': top_left_y,
                'xmax': bottom_right_x,
                'ymax': bottom_right_y
            }]

        # create pascel voc file with annotation information
        save_path_file = f"{os.getcwd()}/../datasets/all/{image}.xml"
        with open(save_path_file, 'w') as f:
            f.write(render_template(
                'annotation.xml',
                folder = 'all',
                filename = f"{image}.jpg",
                path = f"{os.getcwd()}/../datasets/all/{image}.jpg",
                database = 'Unknown',
                width = w,
                height = h,
                depth = c,
                segmented = 0,  # no segmentation data
                objects = rccarobjects
            ))

        new_image = int(image) + 1 if int(image) + 1 <= num_images else 1
        return redirect(f"/?image={new_image}", code=302)
    else:
        abort(405)
