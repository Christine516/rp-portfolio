# You might need to add more of these import statements as you implement your controllers.
from app import app
from flask import Flask, redirect, url_for, render_template, request, session
from helpers import GENRES_LIST, get_score, clear_score
from firebase import firebase
from firebase import firebase



@app.route('/', methods=['GET', 'POST'])
def welcome():


    db = firebase.FirebaseApplication('https://dj-183-5656c.firebaseio.com/', None)
    top_level = db.get('/', None)
    top_list = []
    for key, value in top_level.items():
        temp = [key,value]
        top_list.append(temp)
    top_list.sort(key = sortSecond, reverse = True)

    top_list = top_list[:5]

    return render_template("welcome.html", top_list = top_list)


def sortSecond(val):
    return val[1]

@app.route('/home', methods=['GET', 'POST'])
def index():

    db = firebase.FirebaseApplication('https://dj-183-5656c.firebaseio.com/', None)
    top_level = db.get('/', None)
    top_list = []
    for key, value in top_level.items():
        temp = [key,value]
        top_list.append(temp)
    top_list.sort(key = sortSecond, reverse = True)

    top_list = top_list[:5]

    db = firebase.FirebaseApplication('https://dj-183-5656c.firebaseio.com/', None)
    top_level = db.get('/', None)

    if request.method == 'POST':
        if 'name' in request.form:
            ming_zi = request.form['name']
            session['name'] = ming_zi
            if session['name'] not in top_level.keys():
                db.put('/',session['name'],0)

    data = {
        "genres": GENRES_LIST,
    }



    if request.method == 'POST':
        if 'choice' in request.form:
            user_input = request.form['choice']
            if user_input == "yes":
                clear_score()

    if 'num_total' not in session:
        session['num_total'] = 0

    if 'num_correct' not in session:
        session['num_correct'] = 0


    if session['num_correct'] > session['num_total']:
        session['num_correct'] = 0
        session['num_total'] = 0
    score = get_score()


    return render_template("index.html", **data, score=score, top_list = top_list)

#location.reload();
#<a href="javascript: location.replace(document.referrer)">Try Again?</a>
