# 📄✏ Cement Strength Prediction Project

Concrete is one of the most widely used construction materials, with its compressive strength being a crucial factor in determining the durability and performance of structures. Predicting the compressive strength of concrete accurately is essential for ensuring the safety and longevity of buildings and infrastructure.

### This project is all about measurment prediction of strength of concrete

## Projct Overflow

### The project includes 3 components Data Ingetion, Data Transformation and Data Trainer with there pipline.

## 1. Data Ingestion
      
      Data is uploaded on mongodb server and retrieve from mongo server.

## 2. Data Transformation

      In this section data has preprocessed and cleaned.The feature engineering did with dataset.

## 3. Model Training

    Experimenting various scikit learn regression model like LinearRegression, LassoRegression, DecisionTreeRegressor, Random Forest Regression, AdaBoostRegressor, Gradient Boost Regression, and Gradient Boost Regression


#### Dataset is taken from Kaggle and stored in mongodb

The dataset we are using is the "Concrete Compressive Strength" dataset. It consists of 1030 instances and 9 attributes, including the target variable, compressive strength. Here's a brief overview of the dataset columns:

➡️ Cement (kg/m^3): The amount of cement in the concrete mixture.

➡️ Blast Furnace Slag (kg/m^3): The amount of blast furnace slag in the concrete mixture.

➡️ Fly Ash (kg/m^3): The amount of fly ash in the concrete mixture.

➡️ Water (kg/m^3): The amount of water in the concrete mixture.

➡️ Superplasticizer (kg/m^3): The amount of superplasticizer in the concrete mixture.

➡️ Coarse Aggregate (kg/m^3): The amount of coarse aggregate in the concrete mixture.

➡️ Fine Aggregate (kg/m^3): The amount of fine aggregate in the concrete mixture.

➡️ Age (days): The curing age of the concrete (in days).

➡️ Compressive Strength (MPa): The target variable representing the concrete's compressive strength.


💿 Installing
1. Environment setup.
```
conda create --prefix venv python==3.9 -y
```
```
conda activate venv/
````
2. Install Requirements and setup
```
pip install -r requirements.txt
```
5. Run Application
```
python app.py
```

🔧 Built with
- flask api
- Python 3.9
- Machine learning
- Scikit learn
- 🏦 Industrial Use Cases

