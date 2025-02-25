import streamlit as st
import requests
from PIL import Image
import io

st.title('Is It A Cat?')

file = st.file_uploader('Upload an image', type=['jpg', 'jpeg'])

if file is not None:
    image = Image.open(file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    img_bytes = file.getvalue()
    files = {'file': img_bytes}
    
    try:
        response = requests.post('http://127.0.0.1:10000/predict', files=files)
        st.write(f"Response Status Code: {response.status_code}")
        st.write(f"Response Content: {response.content}")
        
        if response.status_code == 200:
            result = response.json().get('result')
            confidence = response.json().get('confidence')
            
            if result == 'cat':
                st.write(f'This is a cat with {confidence*100:.2f}% confidence.')
            elif result == 'not a cat':
                st.write(f'This is not a cat with {confidence*100:.2f}% confidence.')
            else:
                st.write("Unexpected result from the API.")
        else:
            st.write("Something went wrong with the API request.")
    except Exception as e:
        st.write(f"An error occurred: {e}")
