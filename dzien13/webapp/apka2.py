from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect

#konwencja taka ze apka bedzie sie nazywac jak nazwa pliku czy name = mojaappka
app = Flask(__name__)
#nie moze byc spacji i enterow po app.route po dekoratowach a przed funckja
@app.route('/')
@app.route('/home')
def home():
    return render_template('welcome.html')
@app.route('/strona1')
def strona1():
    return "no lewy idzie ci zajebiscie :D"
@app.route('/luk2')
def luk2():
    return render_template('l22.html')
#app.run()
@app.route('/luk')
def luk():
    return render_template('layout.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/register2', methods=['GET', 'POST'])
def register2():
    if request.method == 'GET':
        return render_template('register2.html')

    if request.form['imie'] == '' or request.form['kurs'] == '':
        return render_template('fail.html')
    else:
        return render_template('succes.html')
#zmienic tryb debugowania
# w trybie debugowania
@app.route('/witaj/<imie>')
def witaj(imie):
    return render_template('witaj.html', imie=imie)

#wszystko co jets w adresie jets stringiem

@app.route('/kwadrat/<int:liczba>')
def kwadrat(liczba):
    return f'kwadrat liczby {liczba} to jest gosciu {liczba**2}'

if __name__ == '__main__':
    app.run(debug=True)