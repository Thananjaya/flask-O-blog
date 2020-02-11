from flask import Flask, render_template, url_for
from forms import UserRegistrationForm, UserSignInForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'abb9614f40e5f6521adb623714cdfc9e'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/registration')
def register():
    form = UserRegistrationForm()
    return render_template('registration.html', title='Sign Up', form=form)

@app.route('/signin')
def signin():
    form = UserSignInForm()
    return render_template('signin.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run(debug=True)