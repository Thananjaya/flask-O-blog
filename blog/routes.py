from blog import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from blog.forms import UserRegistrationForm, UserSignInForm
from blog.models import User, Post

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

@app.route('/registration', methods=['GET', 'POST'])
def register():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email=form.email.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('signin'))
    return render_template('registration.html', title='Sign Up', form=form)

@app.route('/signin')
def signin():
    form = UserSignInForm()
    return render_template('signin.html', title='Sign In', form=form)
