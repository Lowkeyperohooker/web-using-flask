from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def show():
    return render_template('index.html')


@app.route('/result/<int:score>')
def result(score):
    # Determine pass or fail based on score
    res = 'Pass' if score >= 50 else 'Fail'
    result = {'Score': score, 'Result': res}
    return render_template('result.html', result=result)


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        try:
            # Get the input marks
            mathh = float(request.form['math'])
            science = float(request.form['science'])
            english = float(request.form['english'])
            
            # Calculate the average score
            total_marks = (mathh + science + english) / 3
            
            # Redirect to result page with the computed score
            return redirect(url_for('result', score=int(total_marks)))
        
        except ValueError:
            # Handle invalid input (non-numeric values)
            error_message = "Please enter valid numbers for all subjects."
            return render_template('index.html', error_message=error_message)

    return redirect(url_for('show'))


if __name__ == '__main__':
    # Set the port dynamically (can be used for Heroku or local)
    PORT = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
