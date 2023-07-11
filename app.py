import json
from flask import Flask, jsonify
from math_generator_basic_math import question
app = Flask(__name__)

@app.route("/")
def index():
    return "math API by Jorge Rojas III"

@app.route('/basic-math')
def basic_math():
    qs = question()
    category = qs[0]
    ques = qs[1]
    answer = qs[2].lower()
    return jsonify({'category': category,
                    'question': ques,
                    'answer': answer})

app.run()