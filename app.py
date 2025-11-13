from flask import Flask, render_template , request
import requests

app = Flask(__name__)
url = 'https://api.nal.usda.gov/fdc/v1/foods/search'
params = {
    'api_key': '1YeHW5ssRNnnsULz2f3nq5ZNYtQWfJYHlbtUwtyQ',
    'query': 'apple'
}



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index1():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('foods.html')

@app.route('/foods')
def get_foods():
    params = {
        'api_key': "1YeHW5ssRNnnsULz2f3nq5ZNYtQWfJYHlbtUwtyQ" ,
        'pageSize': 10
    }
    # read the search term from query string (e.g., /foods?food_name=apple)
    food_name = request.args.get('food_name', '').strip()
    if not food_name:
        food_name = 'apple'
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
