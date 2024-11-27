#importing required libraries

from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import joblib
import pickle
warnings.filterwarnings('ignore')
from feature import FeatureExtraction

#gbc = joblib.load('model/phishing_url_model.joblib')

file = open("gbc_model.sav","rb")
gbc = pickle.load(file)
file.close()


app = Flask(__name__)

'''


'''

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if 'url' not in data:
        return jsonify({'error': 'A URL is required!'}), 400

    url = data['url']

    obj = FeatureExtraction(url)
    x = np.array(obj.getFeaturesList()).reshape(1,30)
    y_pred = gbc.predict(x)[0]
    
    response = {
        'url': url,
        'prediction': int(y_pred),
        'message': 'Safe' if y_pred == 1 else 'Unsafe'
    }
    return jsonify(response), 200
    '''if request.is_json:
        data = request.get_json()
        url = data.get("url")

        if not url:
            return jsonify({'error': 'A URL is required!'}), 400
        
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,30) 

        y_pred =gbc.predict(x)[0]   # 1 is safe, -1 is unsafe
        
        
        response = {
            'url': url,
            'prediction': y_pred,
            'message': 'Safe' if y_pred == 1 else 'Unsafe'
        }
        return jsonify(response), 200
        #y_pro_phishing = gbc.predict_proba(x)[0,0]
        #y_pro_non_phishing = gbc.predict_proba(x)[0,1]
        # if(y_pred ==1 ):
        #pred = "It is {0:.2f} % safe to go ".format(y_pro_phishing*100)
        #return render_template('index.html',xx =round(y_pro_non_phishing,2),url=url )
    return jsonify({'error': 'Invalid input, please send a JSON request.'}), 400
'''

if __name__ == "__main__":
    app.run(debug=True)
