from flask import Flask, request, render_template
import pickle
import numpy as np
import os

# Load the trained model
with open('classifier_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Initialize the Flask app
app = Flask(__name__)

# Define a test route to check if the server is working
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # Render your input form here

@app.route('/health')
def health_check():
    return "Healthy", 200

# Define the route for the prediction API
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON request data
    data = request.form

    # Extract input values
    GP = int(data['GP'])
    MIN = float(data['MIN'])
    PTS = float(data['PTS'])
    FGM = float(data['FGM'])
    FGA = float(data['FGA'])
    threePM = float(data['3P Made'])
    threePA = float(data['3PA'])
    FTM = float(data['FTM'])
    FTA = float(data['FTA'])
    OREB = float(data['OREB'])
    DREB = float(data['DREB'])
    AST = float(data['AST'])
    STL = float(data['STL'])
    BLK = float(data['BLK'])
    TOV = float(data['TOV'])

    # Calculate FG% and 3P%
    FG_percentage = (FGM / FGA * 100) if FGA > 0 else 0  # Avoid division by zero
    threeP_percentage = (threePM / threePA * 100) if threePA > 0 else 0  # Avoid division by zero
    Threethrow_percentage = (FTM / FTA * 100) if FTA > 0 else 0  # Avoid division by zero

    # Calculate total rebounds
    total_rebounds = OREB + DREB

    # Prepare the features array for the model
    features = np.array([GP, MIN, PTS, FGM, FGA, FG_percentage, threePM, threePA, threeP_percentage,
                         FTM, FTA, Threethrow_percentage,
                         OREB, DREB, total_rebounds, AST, STL, BLK, TOV]).reshape(1, -1)

    # Check the length of features to debug
    print("Features array length:", features.shape[1])  # This should print the number of features

    # Make a prediction using the loaded model
    prediction = model.predict(features)

    # Map prediction to a user-friendly message
    if prediction[0] == 1:
        message = "Career predicted to last 5 years or more."
    else:
        message = "Will not make it more than 5 years."

    # Return the prediction as a JSON response
    return render_template('result.html',
                           prediction=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
