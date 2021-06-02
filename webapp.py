from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__, template_folder='Templates')


@app.route("/")
def render_main():
    print("RunningMain")
    with open('cancer.json') as cancer_data:
        states = json.load(cancer_data)
    return render_template('page1.html')
@app.route("/p1")
def render_first():
    return render_template('page1.html')
@app.route("/p2")
def render_first2():
    return render_template('page2.html')
@app.route("/p3")
def render_first3():
    return render_template('page3.html')
with open('cancer.json') as cancer_data:
    counties = json.load(cancer_data)
if 'counties' in request.args:
    return render_template('page2.html', states = get_state_options(counties), Total_Rate = Total_Rate(get_state(request.args['counties'],counties), counties), counties = get_State_options(get_state(request.args['counties'],counties),counties), Total_Rate = get_Total_Rate(request.args['counties'],counties))
if 'states' in request.args:
    return render_template('page2.html', states = get_state_options(counties), Total_Rate = Total_Rate(request.args['states'], counties), counties = get_State_options(request.args['states'],counties))
elif 'states' not in request.args and 'counties' not in request.args:
    return render_template('page2.html', states = get_state_options(counties))
    

def get_state_options(counties):
    states = []
    print("RunningOP")
    for data in counties:
        if data["State"] not in states:
            states.append(data["State"])
    options = ""
    for data in states:
        options = options + Markup("<option value=\"" + str(data) + "\">" + str(data) + "</option>")
    return options

def Total_Rate(state, counties):
    print("RunningAge")
    points = float(0)
    total = float(0)
    for issued in counties:
        if issued["State"] == state:
            total = issued["Total"]["Rate"]
    return total
def get_State_options(states,counties):
    issuedlist = []
    print("RunningCOP")
    for issued in counties:
        if issued["State"] == states :
            issuedlist.append(["State"])
    options = ""
    for data in issuedlist:
        options = options + Markup("<option value=\"" + str(data) + "\">" + str(data) + "</option>")
    return options
    
def get_Total_Rate(issued, counties):
    print("RunningCAge")
    for issued1 in counties:
        if issued1["State"] == issued:
            return issued1["Total"]["Rate"]
 
def get_state(issued, counties):
    print("RunningState")
    state = ""
    for data in counties:
        if data["State"] == issued:
            state = data["State"]
    return state
    return render_template('page2.html')

        
  

if __name__ == "__main__":
    app.run(debug=True)
