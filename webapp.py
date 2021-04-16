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

def total_rate(states):
    print("RunningRate")
    points = float(0)
    total = float(0)
    for state in states:
        if state["State"] == state:
            total = total + state["Total"]["Rate"]
            points=points + 1
    avg = float(total//points)
    return avg

if __name__ == "__main__":
    app.run(debug=True)
