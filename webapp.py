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


        
  

if __name__ == "__main__":
    app.run(debug=True)
