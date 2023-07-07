# Android Client

## Set up

Download the training and testing data from <https://www.dropbox.com/s/coeixr4kh8ljw6o/cifar10.zip?dl=1> and extract them to `app/src/main/assets/data`.

Download the TFLite model from <https://github.com/FedCampus/dyn_flower_android_drf/files/11858642/cifar10.zip> to `app/src/main/assets/model/cifar10.tflite`.

## Run the demo

Install the app on *physical* Android devices and launch it.

*Note*: the highest tested JDK version the app supports is 16; it fails to build using JDK 19 on macOS.

In the user interface, fill in:

- Device number: a unique number among 1 ~ 10.
    This number is used to choose the partition of the training dataset.
- Server IP: an IPv4 address of the computer your backend server is running on. You can probably find it in your system network settings.
- Server port: 8080, if you use `../server.py`.

Push the first button and load the dataset. This may take a minute.

Push the second button and start the training.
