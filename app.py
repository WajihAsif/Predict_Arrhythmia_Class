import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return(render_template('index.html'))
    if request.method == 'POST':
    
        var15 = request.form['var15']
        var167 = request.form['var167']
        var5 = request.form['var5']
        var228 = request.form['var228']
        var93 = request.form['var93']
        df = pd.DataFrame([[var15, var167, var5, var228, var93]],
                                       columns=['var15', 'var167', 'var5', 'var228', 'var93'])
        # replace ? with nan and nan with most frequent values of each columns
        df = df.apply(lambda x: x.replace('?',np.nan))
        df = df.apply(lambda x:x.fillna(x.value_counts().index[0]))
        df = df.apply(lambda col:pd.to_numeric(col, errors='coerce'))
        
        prediction = model.predict(df)
    
        output = round(prediction[0], 2)
    
        return render_template('index.html', prediction_text='Predicted Arrhythmia class should be {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)


