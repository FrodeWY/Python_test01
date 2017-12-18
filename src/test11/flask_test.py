import json

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['Get', 'Post'])
def home():
    l=[1,2,3,4]
    person={"name":'wangyang','list':l}
    return render_template('home.html',person=person)


@app.route('/signin', methods=['Get'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['Post'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>hello admin</h3>'

    return 'Bad username or password'


@app.route('/urlValue/<id>/')
def url_value(id):
    print(id)
    return json.dumps(id)


@app.route('/getjson', methods=['get'])
def url_get():
    args_get = request.args.get('params', default='13')
    return "<h1>%s</h1>" % json.dumps(args_get)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=False)
