import pandas as pd
from joblib import load
from tensorflow.keras.models import load_model

# Load the trained model
dl_model = load_model('trained-models/deep_learning_model.h5') 
# dl_model = load_model("trained-models/gradient_boosting_model.joblib")
def predictParkinson(test_case):
    print(test_case)
    # Convert the test_case dictionary to a DataFrame
    test_df = pd.DataFrame([test_case])  # Note: Wrap test_case in a list to handle single row DataFrame
    # Drop unnecessary columns
    columns_to_drop = [
        'MDVP:Jitter(Abs)',
        'MDVP:RAP',
        'MDVP:PPQ',
        'Shimmer:APQ5',
        'MDVP:APQ',
        'Shimmer:DDA'
    ]
    test_df = test_df.drop(columns_to_drop, axis=1)
    
    dl_prediction = dl_model.predict(test_df.values).argmax(axis=1)
    
    return int(dl_prediction[0])
    # Make predictions using the loaded deep learning model
    # try :
    #     dl_prediction = dl_model.predict(test_df.values).argmax(axis=1)
    # except :
    #     print("in the detect ")    
    
    return dl_prediction[0]

# Example test case (same as provided)
test_case = {
    'MDVP:Fo(Hz)': 119.99200,
    'MDVP:Fhi(Hz)': 157.30200,
    'MDVP:Flo(Hz)': 74.99700,
    'MDVP:Jitter(%)': 0.00784,
    'MDVP:Jitter(Abs)': 0.00007,
    'MDVP:RAP': 0.00370,
    'MDVP:PPQ': 0.00554,
    'Jitter:DDP': 0.01109,
    'MDVP:Shimmer': 0.04374,
    'MDVP:Shimmer(dB)': 0.42600,
    'Shimmer:APQ3': 0.02182,
    'Shimmer:APQ5': 0.03130,
    'MDVP:APQ': 0.02971,
    'Shimmer:DDA': 0.06545,
    'NHR': 0.02211,
    'HNR': 21.03300,
    'RPDE': 0.414783,
    'DFA': 0.815285,
    'spread1': -4.813031,
    'spread2': 0.266482,
    'D2': 2.301442,
    'PPE': 0.284654153
}
# print(predictParkinson(test_case))
# Print the prediction
