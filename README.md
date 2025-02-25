# Is It A Cat?

A web app to classify pictures into two categories: cat and not cat.

## Project Overview
A convolutional neural network (CNN) was trained on a dataset of ~30,000 cat images and ~25,000 images of other animals. The data was procured through multiple sources and the merged manually. Backend uses a Flask API to make predict calls while the frontend is constructed using Streamlit for simplicity. Code for the CNN is located in the Python notebook with the trained model being the .keras file, Flask and Streamlit app folders hold the script for the backend and frontend, test_call is a local script for testing the API on the stock image.

## Tools Used
- Python
- Libraries:
    - tensorflow, sklearn (for model)
    - kaggle, open cv (for data loading)
    - numpy, pandas, matplotlib, pillow (for preprocessing)
    - Flask (for backend API)
    - Streamlit (for user file upload)
  - Render
  - Jupyter

## Results:
CNN with 1m parameters achieves 96% accuracy on test set however, model sometimes gets confused on animals that are technically cats but differ from the typical house or small cat, tigers being one such animal.

## Possible Next Steps:
- Increase size of dataset to encompass similar animals that model gets confused on
- Hyperparameter tuning with scikit-learn
- Possible data augmentation on existing data to increase model's ability to generalize
- Accept different file formats such as PNG

# \color{red}NOTE}$$
