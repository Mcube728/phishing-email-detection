from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import joblib
import pickle
warnings.filterwarnings('ignore')
from feature import FeatureExtraction

with open('model/gbc_model.sav', 'rb') as model_file:
    gbc = pickle.load(model_file)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if 'urls' not in data:
        return jsonify({'error': 'No URLs provided!'}), 400
    urls = data['urls']
    response = { 'urls':[] }
    for url in urls:
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,30)
        y_pred = gbc.predict(x)[0]
        url_result = {
            'url': url,
            'prediction': int(y_pred),
            'message': 'Safe' if y_pred == 1 else 'Unsafe'
        }
        response['urls'].append(url_result)
    return jsonify(response), 200
    

if __name__ == "__main__":
    app.run(debug=True)
