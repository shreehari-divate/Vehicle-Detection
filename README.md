# Vehicle-Detection
This is a vehicle detection project which detects different types of vehicles from an image or a video. Vehicle detection is used for various purposes such as traffic control, autonomous vehicle etc.

## Aim
<br>To detect different types of vehicles in a given image or a video 

## Technologies used
<br>Python
<br>OpenCV
<br>YOLO

## Source
<br>Dataset is taken from open source platform RoboFlow.

## WorkFlow
Step1: Getting the data from Roboflow.
Step2: Installing necessary libraries.
Step3: Importing required libraries into my workspace which is Pycharm IDE.
Step4: I have used YOLOV8m which is a pre trained model on my train set followed by downloading the weights for my test set.  
Step5: Finally evaluating the model on a video containing various vehicles.
NOTE: The whole process can be done on google colab itself, for this project I tried it this way.

## Results
<br>Labels: 
<br>
![labels](https://github.com/shreehari-divate/Vehicle-Detection/assets/147906812/651c9fd1-cb87-4c6d-ac9c-555d78e817a7)
<br> Prediction:
<br>
![pred](https://github.com/shreehari-divate/Vehicle-Detection/assets/147906812/61bde72b-ad3b-4df2-9f6d-b555b2f67f11)

## Conclusion
<br>I can say that model performed well considering the dataset and its quality. It was not completely perfect as model was struggling to differentiate between bus and truck and car and ambulance. This might be because of various reason such as angle of photo taken or lighting or we could to try out on other models too. Overall its prediction was good.

<br>Check out drive link:
