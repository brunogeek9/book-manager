from app import app
from flask import render_template, request
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/report")
def report():
    username = request.args.get('username')
    contuc = 0
    contlc = 0
    for lt in username:
        if lt.islower():
            contlc = contlc+1
    for lt in username:
        if lt.isupper():
            contuc = contuc+1
    endn = username[-1].isdigit() 
    print(endn)
    print(contlc)
    print(contuc)
    return render_template('report.html',username=username,contlc=contlc,contuc=contuc,endn=endn)