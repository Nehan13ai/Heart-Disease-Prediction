from flask import Flask, render_template, request
from model import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def make_prediction():
    input_data = [
        float(request.form.get('age')),
        float(request.form.get('sex')),
        float(request.form.get('cp')),
        float(request.form.get('trestbps')),
        float(request.form.get('chol')),
        float(request.form.get('fbs')),
        float(request.form.get('restecg')),
        float(request.form.get('thalach')),
        float(request.form.get('exang')),
        float(request.form.get('oldpeak')),
        float(request.form.get('slope')),
        float(request.form.get('ca')),
        float(request.form.get('thal'))
    ]
    prediction = predict(input_data)
    result = "The Person has Heart Disease" if prediction == 1 else "The Person does not have Heart Disease"
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
