import streamlit as st
import requests
from PIL import Image
import io

st.title('Is It A Cat?')

file = st.file_uploader('Upload an image', type=['jpg'])

if file is not None:
    image = Image.open(file)
    st.image(image, caption='Uploaded Image.', use_container_width=True)
    img_bytes = file.getvalue()
    file = {'file': img_bytes}
    response = requests.post('https://isitacatapi.onrender.com/predict', files=file)
    result = response.json()['result']
    confidence = response.json()['confidence']
    if result == 'cat':
        st.write(f'This is a {result} with {confidence*100:.2f}% confidence.')
    elif result == 'not a cat':
        st.write(f'This is {result} with {confidence*100:.2f}% confidence.')
