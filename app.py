# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
# Load the regression model
regressor = pickle.load(open('model1.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    med_earn = int(request.form['med_earn'])
    per = float(request.form['per'])
    age = int(request.form['age'])
    cohort = float(request.form['cohort'])
    enroll = int(request.form['enroll'])
    hh_income = int(request.form['hh_income'])
    med_debt = int(request.form['med_debt'])
    tot_share = int(request.form['tot_share'])
    avg_cost = int(request.form['avg_cost'])
    per_uc = float(request.form['per_uc'])

    data = [[med_earn, per, age, cohort, enroll, hh_income, med_debt, tot_share, avg_cost, per_uc]]
    if (
            med_earn == 0 and per == 0 and age == 0 and cohort == 0 and enroll == 0 and hh_income == 0 and med_debt == 0 and tot_share == 0 and avg_cost == 0 and per_uc == 0):

        my_prediction = [0]
    else:
        my_prediction = regressor.predict(data)

        if my_prediction[0] == 0:
            pred_text = 'The repayment rate of the student is 0'
            return render_template('index.html',
                                   prediction_text=pred_text)
        else:
            pred_text = 'The repayment rate of the student is ' + str(np.round(my_prediction[0],2))
            return render_template('index.html',
                                   prediction_text=pred_text)


if __name__ == "__main__":
    app.run(debug=True)