from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

class ScientificCalculator:
    @staticmethod
    def square_root(x):
        if x < 0:
            raise ValueError("Square root of negative number is not allowed")
        return math.sqrt(x)

    @staticmethod
    def factorial(x):
        if x < 0:
            raise ValueError("Factorial of negative number is not defined")
        return math.factorial(x)

    @staticmethod
    def natural_log(x):
        if x <= 0:
            raise ValueError("Natural logarithm undefined for non-positive values")
        return math.log(x)

    @staticmethod
    def power(base, exponent):
        return math.pow(base, exponent)


@app.route("/square-root", methods=["POST"])
def square_root():
    data = request.json
    try:
        result = ScientificCalculator.square_root(data["number"])
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/factorial", methods=["POST"])
def factorial():
    data = request.json
    try:
        result = ScientificCalculator.factorial(int(data["number"]))
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/natural-log", methods=["POST"])
def natural_log():
    data = request.json
    try:
        result = ScientificCalculator.natural_log(data["number"])
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/power", methods=["POST"])
def power():
    data = request.json
    try:
        result = ScientificCalculator.power(data["base"], data["exponent"])
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)