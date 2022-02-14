from flask import Flask, session

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Witaj świecie tu Flask'

@app.route('/login')
def do_login() -> str:
    session['logged_in']=True
    return 'Teraz jesteś zalogowany'

app.secret_key = 'NigdyNieZgadniesz'

@app.route('/logout')
def do_logout() -> str:
    del session['logged_in']
    return 'Teraz jesteś wylogowany'

@app.route('/status')
def status() -> str:
    if 'logged_in' in session:
        return 'W tej chwili jesteś zalogowany'
    return 'NIE jesteś zalogowany'

@app.route('/page1')
def page1() -> str:
    return 'To jest strona 1'

@app.route('/page2')
def page2() -> str:
    return 'To jest strona 2'

app.secret_key = 'NigdyNieZgadniesz'

if __name__ == '__main__':
    app.run(debug=True)