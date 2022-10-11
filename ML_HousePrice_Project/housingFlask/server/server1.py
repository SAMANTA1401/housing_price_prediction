from flask import Flask, request, jsonify
import util1
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations':util1.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price', methods=['GET','POST'])
def predict_home_price():
    if request.method == 'POST':
        total_sqft =float( request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        response = jsonify({
            'estimated_price': util1.get_estimated_price(location,total_sqft,bhk,bath)
        })
        response.headers.add('Access-Control-Allow-Origin','*')
        return response




if __name__ == "__main__":
    print(" starting")
    util1.load_saved_artifacts()
    app.run(port=8000,debug=True)