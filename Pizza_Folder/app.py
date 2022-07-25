import re
from django.shortcuts import render
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/owner", methods=["GET", "POST"])
def manager():
    default_value = '0'
    global data
    global data2
    global data3
    data = request.form.get('NewTopping')
    data2 = request.form.get('NewTopping2')
    data3 = request.form.get('NewTopping3')
    if request.method == "POST":
        print (data)
        if request.form.get('NTopping') == 'Add_Topping':
            return render_template ("newtopping.html")
    return render_template ("manager.html", value=data, value2=data2, value3=data3)
    # f"<h1> {data}</h1>"

@app.route("/chef", methods=["GET", "POST"])
def chef():
    global option
    option = request.form.get('opt')
    option2 = request.form.get('opt2')
    option3 = request.form.get('opt3')
    sauce1 = request.form.get('opt0')
    sauce2 = request.form.get('2opt0')
    sauce3 = request.form.get('3opt0')

    if request.method == 'POST':
        print(option)
        if request.form.get('CPizza') == 'Create_Pizza':
            return render_template("newpizza.html", value=data, value2=data2, value3=data3)
        

        elif  request.form.get('DPizza') == 'Delete_Pizza':
            print("DPizza")
        else:
            pass
    elif request.method == 'GET':
        print("Working")
    return render_template("chef.html", value=data, tlist=option, tlist2=option2, tlist3=option3, slist1=sauce1, slist2=sauce2, slist3=sauce3)


@app.route('/json')
def json():
    return render_template('json.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')