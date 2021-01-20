# DEPLOYING SCORE CARD MODEL: LENDING CLUB LOAN SCORE CARD PREDICTION MACHINE LEARNING MODEL

Lending club is an American loan lending company. It helps to pay high interest debt and save money as they have low interest rate compared to the market. People, usually students took loan to pay debt, buy computer, buy bike etc. Thy publish data of their borrowers anonymusly. 

As a lending company they need to make a score cards. Generally two types of score cards are made by the analysts of the company. One for the people who apply for loan and another for the current borrowers. Both models are build based on the past experiences. In the later model we predict the probability of a borrower to return the debt. As a lending company this important to deduce. Depending on the probability we assign score to the borrower to help business professionals to understand the "quality" of borrower and decide further steps.

This model is based on the data of borrowers from the year 2007 to 2011. The data is collected from Data World. Click [here](https://data.world/jaypeedevlin/lending-club-loan-data-2007-11) to get the data. There are two files available in the website. One contains the data, another contains the dictionary with the description/ meaning of the atributes.

## Model Description:
This model uses Logistic Regression to predict the probability of default for a borrower. This model is build to deploy on the web, such that actual business professionals can use it to assign the score to the borrowers. 

This is a **End-to-End Machine Learning Project** including all the preprocessing steps and finally using Logistic Regression to predict the probability. Finally we deploy it. Web-Deployment will be added to the later versions.

Model is built upon the `sklearn`'s `LogisticRegression`. 

## Command Line Interface: Instructions to use the package on terminal

Clone the package on the local on the local device. Go to the `scorecard_model` folder , which is the parent directory of the `scorecard_model/scorecard_model` folder. Install the requirements.txt file with pip
```pip
pip install -r requirements.txt
```
. Now from `< root >/applications/scorecard_model` run  python interpreter, ipython console, qtconsole, jupyter notebook, jupyter lab or any other python interpreter interface of your choice. Then run 

```python
from scorecard_model import train_model
```
This would  import the model and train it. Even if the data is missing it would download the data. Then it saves the model and all the imputation steps, so the model could be reproduced. 

To train the model on newer version of the data save the data into the `datasets` folder. Just, the data structure needed to be strong.

After training, to use the model for prediction run:
```python
from scorecard_model import predict
```

Future versions will include more functionality.

#### Data Analysis and Model Building:
Analysis is done on the kaggle's notebook platform. Project is divided into three parts. Click to go to the kaggle notebooks.

[**1. Loan Score Card Modelling: Data Analysis**](https://www.kaggle.com/aniruddhamandal/1-loan-score-card-modelling-dataanalysis)

[**2. Loan Score Card Modelling: Feature Engineering**](https://www.kaggle.com/aniruddhamandal/2-loan-score-card-modelling-feature-engineering)

[**3. Loan Sore Card Modellin: Model Building**](https://www.kaggle.com/aniruddhamandal/3-loan-score-card-modelling-model-building)
