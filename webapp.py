from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    print("RunningMain")
    with open('cancer.json') as cancer_data:
        states = json.load(cancer_data)
        
        if 'states' in request.args:
        return render_template('page2.html', states = get_state_options(states), total_rate = total_rate(request.args['states']))

    def get_state_options(states):
    states = []
    print("RunningOP")
    for data in states:
        if data["State"] not in states:
            states.append(data["State"])
    options = ""
    for data in states:
        options = options + Markup("<option value=\"" + data + "\">" + data + "</option>")
    return options

