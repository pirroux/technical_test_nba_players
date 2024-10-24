# NBA Player Longevity Prediction

## Description
This project aims to predict whether NBA players will last more than 5 years in the league based on various features. The model is built using XGBoost and incorporates techniques to handle class imbalance.

## Table of Contents
- Installation
- Usage
- Model Details
- Data
- Deployment on Google cloud through Docker
- Contributing
- License
- Acknowledgments

## Installation
1. Clone the repository:
no repo on github for this technical test

2. Install dependencies:
pip install -r requirements.txt

3. To make predictions, visit the website and enter inputs:
https://mpdata-768760688310.europe-west2.run.app/

4. Data
The model is trained on NBA player statistics, including performance metrics, team data, and player characteristics. Data preprocessing steps included scaling and SMOTE for class imbalance.

5. Deployment:
XGB Model Flask Application
This repository contains a Flask web application that serves an XGBoost model to make predictions. The application is containerized using Docker and deployed on Google Cloud Run.

Project Structure
.
├── app.py               # Main Flask application
├── model.pkl            # Pre-trained XGBoost model
├── Dockerfile           # Dockerfile to containerize the app
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

Running Locally
To run the application locally, follow these steps:

Clone the repository: in this case the repo was not on github (request from mpdata)

Copy the following code:

git clone <repository-url>
cd <repository-directory>

Build the Docker image:

Copy the following code:

docker build -t xgb-model-image .
Run the Docker container:

Copy the following code:

docker run -p 8080:8080 xgb-model-image
Access the application:

Open your browser and navigate to http://localhost:8080.

Deploying to Google Cloud Run
To deploy the application to Google Cloud Run, follow these steps:

Prerequisites
You need a Google Cloud project with billing enabled.
You need to have the Google Cloud SDK installed and authenticated.
Tag the Docker image for Google Container Registry (GCR):

If you haven't already, tag your image with your Google Cloud project ID. Replace <local-image-id> with your Docker image ID and <project-id> with your Google Cloud project ID.

Copy the following code:

docker tag <local-image-id> gcr.io/<project-id>/xgb-model-image:latest
Example:

Copy the following code:

docker tag c4ff4901b78a gcr.io/mpdata-439311/xgb-model-image:latest
Push the image to GCR:

Push the tagged image to GCR:

Copy the following code:

docker push gcr.io/<project-id>/xgb-model-image:latest
Example:

Copy the following code:

docker push gcr.io/mpdata-439311/xgb-model-image:latest
Deploy to Cloud Run:

Use the gcloud command to deploy the image to Google Cloud Run. Replace <project-id> with your project ID and adjust the region if necessary:

Copy the following code:

gcloud run deploy xgb-model-image \
--image gcr.io/<project-id>/xgb-model-image:latest \
--platform managed \
--region europe-west2 \
--allow-unauthenticated
Example:

Copy the following code:

gcloud run deploy xgb-model-image \
--image gcr.io/mpdata-439311/xgb-model-image:latest \
--platform managed \
--region europe-west2 \
--allow-unauthenticated
Access the deployed application:

After deployment, you'll receive a URL where your application is running. You can access it by visiting that URL in your browser.

Updating the Deployment
To update the application after making changes:

Rebuild the Docker image:

Copy the following code:

docker build -t gcr.io/<project-id>/xgb-model-image:latest .
Push the updated image to GCR:

Copy the following code:

docker push gcr.io/<project-id>/xgb-model-image:latest
Deploy the updated image:

Copy the following code:

gcloud run deploy xgb-model-image \
--image gcr.io/<project-id>/xgb-model-image:latest \
--platform managed \
--region europe-west2 \
--allow-unauthenticated

6. Contributing
no contributors

7. License
No license

8. Acknowledgments
XGBoost Documentation
myself :-)
