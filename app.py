import joblib
from flask import Flask, request, jsonify, render_template

#loading models
cv=joblib.load("models/cv.joblib")
model=joblib.load("models/model.joblib")

#Flask App Instance creation
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",result_image_display=None)



@app.route('/predict', methods=['POST'])
def predict():
    req = request.form.to_dict()
    #print(req)
    message=req["sentence"]
    
    
    prediction=model.predict(cv.transform([message,]))
    
    result = {
        'prediction': f"{prediction}"
    }
    #print(prediction[0])
    if prediction[0]=="ham":
        image_url="static/images/not_a_spam.jpg"
    else:
        image_url="static/images/spam.jpg"
        
    return render_template("index.html", title="Home",result_image_url=image_url,result_image_display=True)

@app.route('/spam-classifier-api', methods=['POST'])
def spam_classifier_api():
    try:
        req = request.get_json()
        
        message=req["sentence"]
        prediction=model.predict(cv.transform([message,]))
    except:
        prediction="Error while processing the request"
    
    
    result = {
        'prediction': f"{prediction}"
    }
    return jsonify(result)
