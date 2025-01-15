from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def show():
    return render_template('index.html')


@app.route('/result/<int:score>')
def result(score):
    res=''
    if score>=50:
        res='Pass'
    else:
        res='Fail'
    result = {'Score':score, 'Result':res}
    return render_template('result.html', result=result)


@app.route('/submit', methods=['POST'])
def submit():
    total_marks = 0
    if request.method == 'POST':
        mathh = request.form['math']
        science = request.form['science']
        english = request.form['english']
        total_marks = (float(mathh) + float(science) + float(english))//3
    return redirect(url_for('result', score=total_marks))

if __name__=='__main__':
    PORT = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=PORT, debug=True)