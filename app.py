from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Jack McDonough!This is my first code update'
@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')
@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')
@app.route('/contact', methods= ['GET', 'POST'])
def contact():  # put application's code here
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')
@app.route('/favorite-course')
def favoritecourse():  # put application's code here
    return render_template('favorite-course.html')


if __name__ == '__main__':
    app.run()
