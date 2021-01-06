from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="datasets")
trainer.setTrainConfig(
  object_names_array=["rccar"],
  batch_size=32,
  num_experiments=3,
  train_from_pretrained_model="pretrained-yolov3.h5"
)
trainer.trainModel()