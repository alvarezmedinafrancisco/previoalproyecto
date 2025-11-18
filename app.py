from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"
API_KEY = "1YeHW5ssRNnnsULz2f3nq5ZNYtQWfJYHlbtUwtyQ"


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")



@app.route("/foods", methods=["GET"])
def get_foods():
    # Leer el nombre de la comida desde la query (?food_name=manzana)
    food_name = request.args.get("food_name", "").strip()

    if not food_name:
        food_name = "apple"  # valor por defecto

    params = {
        "api_key": API_KEY,
        "query": food_name,
        "pageSize": 12
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        foods = data.get("foods", [])
        return render_template("foods.html", foods=foods, food_name=food_name, error=None)
    except requests.exceptions.RequestException as e:
        error_message = f"Ocurrió un error al consultar la API: {e}"
        return render_template("foods.html", foods=[], food_name=food_name, error=error_message)


if __name__ == "__main__":
    app.run(debug=True)
