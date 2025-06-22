import streamlit as st
from PIL import Image
import os
import numpy as np
import gzip
import pickle


from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# Load the generator model
@st.cache_resource
def load_generator_model():
    return load_model("saved_generator_model.keras")


def main():
    # Título de la aplicación
    st.title("Hadwritten Digit Image Generator")

        
    st.write("""
    ### What can you do?
    You can generate images of hanswritten digits 0-9. Generate syntethic MNIST-like images using cGan model.
    
    """)
    st.image('MNISTpicture.png', caption="MNIST")

    selected_digit = st.selectbox("Select a digit (0–9) to generate images:", list(range(10)))


if __name__ == "__main__":
    main()
