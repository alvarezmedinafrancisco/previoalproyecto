from flask import Flask, render_template , request
import requests

app = Flask(__name__)

api_key = '1YeHW5ssRNnnsULz2f3nq5ZNYtQWfJYHlbtUwtyQ'
url = 'https://api.nal.usda.gov/fdc/v1/foods/search'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index1():
    return render_template('index.html')

@app.route('/foods')
def acerca():
    return render_template('foods.html')

@app.route('/foods')
def get_foods():
    params = {
        'api_key': api_key,
        'pageSize': 10
    }
    food_name = request.get('food_name')
    params['query'] = food_name
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        foods = data.get('foods', [])
        return render_template('foods.html', foods=foods, food_name=food_name)
    except requests.exceptions.RequestException as e:
        error_message = f"An error occurred: {e}"
        return render_template('foods.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
