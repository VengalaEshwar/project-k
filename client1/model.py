from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np


# Load the model with custom objects
model = load_model("keras_Model.h5", compile=False)


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model

# Load the labels
class_names = open("labels.txt", "r").readlines()
image = cv2.imread('32 (8).jpg')
image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
image = (image / 127.5) - 1

prediction = model.predict(image)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

print("Class:", class_name[2:], end="")
print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
