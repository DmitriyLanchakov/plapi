from flask import Flask, render_template


app = Flask(__name__)


@app.route('/user/')
def user():
    return render_template('user.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=8001, debug=True)