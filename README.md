# AutoML-Spam-Classifier
A flask application that uses Google's Natural Language AutoML to get a prediction on a given SMS message.


![](https://i.imgur.com/D0epCeH.png)

## Requirements
> 1. Have a trained AutoML model (from Natural Language)
> 2. Set-up IAM permissions for Google AppEngine to make predictions (with the AutoML role)

## Instructions (for running in a local environment)
1.     Revise lines 5 and 6 of main.py to reflect your project and model-id. Note that Model ID is not the name of the model.
2.     git clone https://github.com/aniquekhawar/aniquekhawar-AutoML-Spam-Classifier.git
3.     sudo apt-get install python3-venv
4.     python3 -m venv venv
5.     source venv/bin/activate venv
6.     cd aniquekhawar-AutoML-Spam-Classifier

>Install system requirements

7.     make install
8.     python main.py
9. Navigate to your local address and test out your model on a local environment.

## Gotchas
> If you are having issues with permissions when running predictions (i.e. 403 errors), you can create a service account and generate an API key (service_account.json). From there, run the following 2 commands to set-up your shell environment for running predictions.
1.     export GOOGLE_APPLICATION_CREDENTIALS=service_account.json
2.     export PROJECT_ID=[SOME-PROJECT-ID]
> From there the Google Cloud Shell should know to use these credentials to allow any predictions to go through.
