# digit recognizer webapp
> Flask web application for deploying a digit recognizer model built using <br /> PyTorch. <br />

>Only works for digits from 0 - 9.

# model's accuracy on each digit
> Test Accuracy of 0: <b> 99% </b>

> Test Accuracy of 1: <b> 99% </b>

> Test Accuracy of 2: <b> 99% </b>

> Test Accuracy of 3: <b> 99% </b>

> Test Accuracy of 4: <b> 99% </b>

> Test Accuracy of 5: <b> 99% </b>

> Test Accuracy of 6: <b> 98% </b>

> Test Accuracy of 7: <b> 98% </b>

> Test Accuracy of 8: <b> 99% </b>

> Test Accuracy of 9: <b> 98% </b>

# overall test tccuracy
> Test Accuracy : <b> 99% </b>

# home page and predictions page
> Upload Image Page <br />
![upload page](images/upload_image.png)

> Uploaded Image <br />
![uploaded image](images/pay-3208060__340.png)

> Predicted Label <br />
![sample prediction](images/sample_prediction.png)

# unique files in the project
> architecture.py <br />
Contains the classifier model's <b>architecture class</b> necessary when <br /> loading the model's checkpoint. <br /> Also contains two methods, <b> get_model() </b>, which loads and returns the model, <br /> and <b> get_tensor() </b> method with takes as a parameter image bytes <br /> from uploaded image, transforms the image's size and color to grayscale, <br /> then returns a tensor.

> inference.py <br />
Contains the <b> get_image_label() </b> method which passes image bytes through <br /> the <b> get_tensor() </b> method, the returned tensor through the model and <br /> returns the <b> predicted label </b>.
