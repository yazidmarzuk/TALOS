from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("LAN_detection/keras_model.h5", compile=False)

# Load the labels
class_names = open("LAN_detection/labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)
camera.set(3,640)
camera.set(4,480)

while True:
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Show the image in a window
    cv2.imshow("LAN Port Detection", image)

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    

camera.release()
cv2.destroyAllWindows()