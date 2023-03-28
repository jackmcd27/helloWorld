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
@app.route('/favorite-course')
def favoritecourse():  # put application's code here
    print('You entered your favorite course as:' + request.args.get('subject') + request.args.get('course_num'))
    return render_template('favorite-course.html')


if __name__ == '__main__':
    app.run()
