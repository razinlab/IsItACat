import requests

url = 'http://127.0.0.1:5000/predict'
img_path = 'istockphoto-144293437-612x612.jpg'

with open(img_path, 'rb') as img:
    files = {'file': img}
    response = requests.post(url, files=files)

print(response.json())