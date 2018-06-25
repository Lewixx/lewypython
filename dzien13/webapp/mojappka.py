from flask import Flask

#konwencja taka ze apka bedzie sie nazywac jak nazwa pliku czy name = mojaappka
app = Flask(__name__)
#nie moze byc spacji i enterow po app.route po dekoratowach a przed funckja
@app.route('/')
@app.route('/home')
def home():
    return 'Hello Lewix Flask'
@app.route('/strona1')
def strona1():
    return "no lewy idzie ci zajebiscie :D"
#app.run()

#zmienic tryb debugowania
# w trybie debugowania

@app.route('/witaj/<imie>')
def witaj(imie):
    return f'eloooo {imie}'

#wszystko co jets w adresie jets stringiem

@app.route('/kwadrat/<int:liczba>')
def kwadrat(liczba):
    return f'kwadrat liczby {liczba} to jest gosciu {liczba**2}'

if __name__ == '__main__':
    app.run(debug=True)