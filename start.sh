cd flask_app
gunicorn -w 1 -b 0.0.0.0:5000 app:app &

cd streamlit_app
streamlit run app.py --server.port 10000 --server.address 0.0.0.0
