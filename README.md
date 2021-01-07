# RC Car Object Detecter - Take 1

This is the first take at creating an object detector for an rc car. [Check out the final result on YouTube](https://www.youtube.com/watch?v=GtMnB0cJqY0) 

## How it Works (it doesnt really)

I'm using [imageai](https://imageai.readthedocs.io/en/latest/) as a layer on top of tensorflow. Honestly this is mostly just a copy and paste of their getting started tutorial. I trained the data on the images from 2 video clips. One from a head mounted GoPro, and one from an iPhone. I think I used about 80% of the images for training and the remaining for validation. **Yes, this was a mistake.** I realized about halfway through annotating a couple thousand images this was a very wrong approach, so it makes sense that I now have a horrible object detector. It performs OK on the video clips the training data came from... go figure.

At the beginning I was thinking I'd be able to run this model on the [official traxxas rustler video](https://www.youtube.com/watch?v=WUAOGLq7PBQ) and pick up the car, but as I already mentioned the model was not up for it. For all I know it just learned where a car typically is within the track I shot the videos on. I need diverse training data. Here is the only image NOT from the clips I got a detection from.

![A traxxas rustler with a bounding box around it.](/random-images-detected/snow-track-3.png)

As you can see its from the same track as the training data, just a different time of year.

## Annotating Data

I annotated by hand almost 3000 images that I pulled from the 2 video clips. I was looking at a couple annotation solutions, but desided I would build my own, web based, annotator. That way I would pick up any device on the network and annotated data without having to install and build an application.

![A screenshot of web browser with an rc car being annotated](/annotator/screenshots/screenshot-4.png)

There are quick keyboard shortcuts for click top left, and bottom right corners on the image, as well as mark the image as difficult and/or truncated. Submitting an annotation saves the data in the Pascal VOC format.
