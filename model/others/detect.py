import pandas as pd
from joblib import load
from tensorflow.keras.models import load_model

# Load the trained models
rfc = load('random_forest_model.joblib')
svc = load('svc_model.joblib')
gbc = load('gradient_boosting_model.joblib')
knn = load('knn_model.joblib')
dl_model = load_model('deep_learning_model.h5')  
# Get test case from user
test_case = {phon_R01_S01_1,119.99200,157.30200,74.99700,0.00784,0.00007,0.00370,0.00554,0.01109,0.04374,0.42600,0.02182,0.03130,0.02971,0.06545,0.02211,21.03300,1,0.414783,0.815285,-4.813031,0.266482,2.301442,0.284654153.
}

# Convert test case to DataFrame
test_df = pd.DataFrame(test_case)

# Predict status using the loaded models
rfc_prediction = rfc.predict(test_df)
svc_prediction = svc.predict(test_df)
gbc_prediction = gbc.predict(test_df)
knn_prediction = knn.predict(test_df)

# Predict status using the deep learning model
dl_prediction = dl_model.predict(test_df.values).argmax(axis=1)

print("Random Forest Classifier Prediction:", rfc_prediction[0])
print("SVC Prediction:", svc_prediction[0])
print("Gradient Boosting Classifier Prediction:", gbc_prediction[0])
print("K-Nearest Neighbors Classifier Prediction:", knn_prediction[0])
print("Deep Learning Model Prediction:", dl_prediction[0])
