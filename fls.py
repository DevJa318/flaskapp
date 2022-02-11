from flask import Flask,render_template,request #redirect
from vsearch import search4letters

app=Flask(__name__)

def log_request(req: 'flask_request', res:str) -> None:
    with open('vsearch.log', 'a') as log:
        print(res, req, file = log)
"""
@app.route('/')
def hello() -> '302':
    return redirect('/entry')
"""
# flaskapp

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


if __name__ == '__main__':
    app.run(debug=True)

    
