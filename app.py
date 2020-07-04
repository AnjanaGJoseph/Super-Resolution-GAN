import streamlit as st 
from PIL import Image
import numpy as np
from ISR.models import RRDN

def predict(img):
        lr_img = np.array(img)
        model = RRDN(weights='gans')
        sr_img = model.predict(np.array(lr_img))
        return (Image.fromarray(sr_img))


st.title("Super Resolution GAN ")
st.subheader("Upload an image which you want to upscale")   
st.spinner("Testing spinner")

uploaded_file = st.file_uploader("Choose an image...", type=("jpg", "png", "jpeg"))

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.')
    st.write("")
    if st.button('Upscale Now'):
        st.write("upscaling...") 
        pred = predict(image)
        st.image(pred, caption='Upscaled Image', use_column_width=True)        