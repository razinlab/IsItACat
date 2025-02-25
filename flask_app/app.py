from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from PIL import Image
import numpy as np
import io

model = tf.keras.models.load_model('cat_classifier.keras')
app = Flask(__name__)
CORS(app)
def prepare_img(image):
    img = image.convert('RGB')
    img = img.resize((64, 64))
    img = np.array(img)
    img = img/255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    image = Image.open(io.BytesIO(request.files['file'].read()))
    image = prepare_img(image)
    prediction = model.predict(image)[0][0]
    result = 'cat' if prediction>=0.5 else 'not a cat'
    confidence = float(prediction) if prediction>=0.5 else 1-float(prediction)
    return jsonify({'result': result, 'confidence': confidence})

if __name__ == '__main__':
    app.run(debug=True)

