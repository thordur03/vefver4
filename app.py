from flask import Flask, render_template,json, session, url_for, request, redirect

import os


app = Flask(__name__)

app.secret_key = os.urandom(8)

vorur = [
    [0,"Peysa","peysa.jpg",2500],
    [1,"Buxur","buxur.jpg",3500],
    [2,"Skór","skor.jpg",1500],
    [3,"Trefill","trefill.jpg",2500],
    [4,"Jakki","jakki.jpg",300],
    [5,"Húfa","hufa.jpg",1000]

]

@app.route("/")
def index():
    return render_template('index.html', v=vorur)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'), 404

@app.errorhandler(500)
def servererror(error):
    return render_template('servererror.html'), 500

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)
    # app.run()