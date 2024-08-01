## Pest Management of Storage Rooms with the use of Image Processing

## Overview

This project work plans the identification of pests in real-time through the webcam along with the help of the ML model. The system recognizes pest such as the squirrels, rats and raccoons hence informing the user and owner of the building through a WhatsApp message the existence of a pest that has a high assurance probability.

## Features

- By means of the webcam, the practice of achieving a live feed while recording is possible.
- Localization of certain pests using a Machine Learning model.
- Notification alarms on the WhatsApp application particularly, if the level of credible pests identification is high.
- Basic directions as to how the setup of the product is done and how the client can use it.

## Prerequisites

- Python 3.9.5
- TensorFlow 2.15.0
- OpenCV
- NumPy
- PyWhatKit

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Yuvadarshan/Storage-rooms-pest-control-using-image-processing.git
cd Storage-rooms-pest-control-using-image-processing

2. Install the required packages

pip install -requirements.txt

3. Ensure keras_model.h5 and lable.txt files are in the same directory.

python main.py

The system will begin analyzing video stream and if it will recognize a pest with high confidence, a WhatsApp message will be sent.

##Configuration

-Change the phone number, and the message in the notification(frame) function in main. You can add or minimize any section of the py to make it a perfect fit for your project.

-Tune the block of detecting based on the confidence in the result.

##File Structure

main.py: For running the pest detection the system follows a main script.

keras_model.h5: file of pre-trained ML model.

labels.txt: It stores the label that used by the model in text file format.

requirements.txt: That is why the list of required packages for this language includes:

##Contributing

Contributions are welcome! Kindly ensure that you create your own branch and then make the necessary change and then make a pull request.


##Acknowledgements

-OpenCV community for having one of the best computer vision library out there.
-For the integration of the WhatsApp, the appropriate library used here is PyWhatKit.

##Contact
G-Mail: myuvadarshan.cse2023@citchennai.net
