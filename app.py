import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import os
import time  # Import time for simulating processing time

# Load your trained model
model = load_model('model.h5')

# Automatically generate class names from training directory
train_dir = './image/train'
class_names = {index: folder for index, folder in enumerate(os.listdir(train_dir))}

# Function to preprocess the uploaded image
def preprocess_image(image):
    image = image.resize((150, 150))  # Resize image
    image = np.array(image) / 255.0    # Scale pixel values
    return np.expand_dims(image, axis=0)  # Add batch dimension

# Streamlit app layout
st.title("Bird Classification App")
st.markdown("""
    Welcome to the Bird Classification App! 🐦

    This application uses a trained deep learning model to classify different species of birds based on the images you upload. 
    Simply select an image of a bird from your device, and click the **Process** button to see the classification result.

    ### Instructions:
    1. Click on the **Choose an image...** button to upload a bird image.
    2. After uploading, click on **Process** to analyze the image.
    3. The app will display the predicted bird species along with the confidence level.

    We hope you enjoy using this application! 
""")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button("Process"):
        # Show a progress bar while processing
        progress_bar = st.progress(0)

        # Simulate processing time
        for i in range(100):
            time.sleep(0.02)  # Simulate some processing time
            progress_bar.progress(i + 1)  # Update progress bar

        # Process the image and predict
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image)

        predicted_index = np.argmax(predictions)
        predicted_bird_name = class_names[predicted_index]
        confidence = predictions[0][predicted_index] * 100

        st.write(f"### Predicted Bird: {predicted_bird_name} ({confidence:.2f}%)")
        st.markdown(f"""
            **Confidence Level:** {confidence:.2f}%
            The model has identified this bird as **{predicted_bird_name}** with a confidence of **{confidence:.2f}%**. 
            If you have any feedback or questions about the predictions, feel free to reach out!
        """)
