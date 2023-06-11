from flask import Flask

app = Flask(__name__)

@app.route('/page1')
def page1():
    return '<h1>Página 1</h1>'

@app.route('/page2')
def page2():
    return '<h1>Página 2</h1>'

@app.route('/page3')
def page3():
    return '<h1>Página 3</h1>'

@app.route('/page4')
def page4():
    return '<h1>Página 4</h1>'

app.run()