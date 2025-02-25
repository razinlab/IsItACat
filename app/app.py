import streamlit as st
from flask import Flask, request, jsonify
from PIL import Image
import io
import tensorflow as tf
import numpy as np
import requests
import os

model = tf.keras.models.load_model('cat_classifier.keras')

app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        try:
            image = Image.open(io.BytesIO(file.read())).convert('RGB')
            image = image.resize((64, 64))
            image = np.array(image) / 255.0
            image = np.expand_dims(image, axis=0)

            prediction = model.predict(image)[0][0]

            result = 'cat' if prediction >= 0.5 else 'not a cat'
            confidence = float(prediction) if prediction >= 0.5 else float(1 - prediction)
            return jsonify({'result': result, 'confidence': confidence})
        except Exception as e:
            return jsonify({'error': str(e)})

def main():
    st.title('Is It A Cat?')

    uploaded_file = st.file_uploader('Upload an image', type=['jpg'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_container_width=True)

        img_bytes = uploaded_file.getvalue()
        files = {'file': img_bytes}

        response = requests.post('http://127.0.0.1:5000/predict', files=files)

        if response.status_code == 200:
            result = response.json()['result']
            confidence = response.json()['confidence']
            if result == 'cat':
                st.write(f'This is a {result} with {confidence*100:.2f}% confidence.')
            elif result == 'not a cat':
                st.write(f'This is {result} with {confidence*100:.2f}% confidence.')
        else:
            st.write(f'Something went wrong: {response.status_code} - {response.text}')  # Include error details

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    if "RUN_STREAMLIT" in os.environ:
        main()
    else:
        app.run(debug=True, host='0.0.0.0', port=port)
