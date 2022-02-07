import vsearch as vsearch
from flask import Flask, render_template, request, redirect

app= Flask(__name__)

#
# @app.route('/')
# def hello() -> str:
#     return redirect('/entry')


@app.route('/search4', methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    letters= request.form['letters']
    title='Here are your results'
    results= str(vsearch.search4letters(phrase, letters))
    return render_template(
        'results.html',
        the_phrase = phrase,
        the_letters = letters,
        the_title = title,
        the_results = results,
    )


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Welcome to search4letter on the web!')


if __name__ == '__main__0':
    app.run(debug=True)
