from imageai.Detection.Custom import CustomObjectDetection
import os

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("datasets/models/detection_model-ex-003--loss-0009.744.h5")
detector.setJsonPath("datasets/json/detection_config.json")
detector.loadModel()

for filename in os.listdir('./datasets/all'):
    if filename.endswith(".jpg"):
        detections = detector.detectObjectsFromImage(input_image=f"datasets/all/{filename}", output_image_path=f"all-images-detected/{filename.zfill(10)}")
        for detection in detections:
            print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
    else:
        continue

