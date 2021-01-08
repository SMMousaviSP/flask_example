from flask import Flask, render_template, request
# from markupsafe import escape
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/<string:name>')
def index(name=None):
    if request.method == 'POST':
        name = request.form['name']
    return render_template('index.html', name=name, method=request.method)
