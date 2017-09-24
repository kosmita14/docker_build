from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print ("ala ma kota")
    return 'Flask Dockerized'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
