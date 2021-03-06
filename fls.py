from flask import Flask,render_template,request,escape #redirect
from vsearch import search4letters

from DBcm import UseDatabase

app=Flask(__name__)

app.config['dbconfig'] = {'host':'127.0.0.1',
        'user':'vsearch',
        'password':'vsearchpasswd',
        'database':'vsearchlogDB',}


def log_request(req: 'flask_request', res:str) -> None:
    
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
        (phrase,letters, ip, browser_string, results)
        values
        (%s, %s, %s, %s, %s)"""
    
        cursor.execute(_SQL,(req.form['phrase'],
                            req.form['letters'],
                            req.remote_addr,
                            req.user_agent.browser,
                            res,
                            ))

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase,letters))
    title = 'Oto Twoje wyniki'

    log_request(request, results)

    return render_template('results.html', the_phrase = phrase,
                          the_letters = letters,
                          the_title = title,
                          the_results = results)
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Witamy na stronie internetowej Search")


@app.route('/viewlog')
def viewlogpage() -> 'html':
    contents = []
    
    
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results
                from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
                
        titles = ['Fraza','Litery','Adres','Przeglądarka','Wyniki']
        
        return render_template('viewlog.html',
                               the_title ="Takie są logi:",
                               the_row_titles = titles,
                               the_data = contents,
                              )

if __name__ == '__main__':
    app.run(debug=True)

    
