from flask import Flask, render_template, jsonify, request, send_file
from src.exception import CustomException
from src.logger import logging as lg
import os,sys
import pandas as pd
from src.utils import load_object
from src.pipeline.train_pipeline import TrainPipeline
from src.pipeline.predict_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/train")
def train_route():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()

        return jsonify("Training Successfull.")

    except Exception as e:
        raise CustomException(e,sys)
    

@app.route("/predict", methods = ['POST', 'GET'])
def predict():
    try:
        if request.method == "POST":
            data = dict(request.form.items())
            print(data)
            df=pd.DataFrame([data])
            print(df)
          
            model_path = os.path.join('artifacts','model.pkl')
            model = load_object(file_path=model_path)

            preds = model.predict(df.iloc[:, :8])
            print(preds)
            return f"The strength prediction is {preds}"
    except Exception as e:
        raise CustomException(e,sys)

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    
    try:


        if request.method == 'POST':
            prediction_pipeline = PredictionPipeline(request)
            prediction_file_detail = prediction_pipeline.run_pipeline()

            lg.info("prediction completed. Downloading prediction file.")
            return send_file(prediction_file_detail.prediction_file_path,
                            download_name= prediction_file_detail.prediction_file_name,
                            as_attachment= True)


        else:
            return render_template('upload_file.html')
    except Exception as e:
        raise CustomException(e,sys)
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug= True)