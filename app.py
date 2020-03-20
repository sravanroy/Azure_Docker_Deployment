from flask import Flask, render_template, request
from scipy.special import boxcox1p
import pandas as pd
import numpy as np
import pickle
app = Flask(__name__)   


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
  
    if request.method == 'POST':
 
        try:
            
            if (float(request.form['OverallQuality']) >= 1 and float(request.form['OverallQuality']) <= 10 ):
                OverallQuality = float(request.form['OverallQuality'])
                OverallQuality_T = boxcox1p(OverallQuality , 0.15)
            else:
                OverallQuality_T = ""
                
            if (float(request.form['LivingArea']) <= 5600 and float(request.form['LivingArea']) >= 400):
                LivingArea = float(request.form['LivingArea'])
                LivingArea_T = boxcox1p(LivingArea , 0.15)
            else:
                LivingArea_T = ""
                
            if (float(request.form['GarageCars']) <= 4 and float(request.form['GarageCars']) >= 0  ):
                GarageCars = float(request.form['GarageCars'])
                GarageCars_T = boxcox1p(GarageCars, 0.15)
            else:
                GarageCars_T = ""
             
            with open('lgb_model.pkl', 'rb') as f:
                ml_model = pickle.load(f)
            pred_args = [OverallQuality_T, LivingArea_T, GarageCars_T]
            pred_args_arr = np.array(pred_args).reshape(1,-1)
  
            model_prediction =  ml_model.predict(pred_args_arr)
            model_prediction = np.expm1(model_prediction)
            model_prediction = round(float(model_prediction), 2)
        except ValueError:
            return "Please check if the values are in the range!"
    return render_template('predict.html', prediction = model_prediction)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = False)
    #app.run(debug = True)

  