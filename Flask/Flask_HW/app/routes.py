from flask import render_template, flash, redirect
from app import app, db
from app.forms import RegisterForm, SignInForm, BlogForm, CarForm
from app.models import User
from flask_login import current_user, login_user


@app.route('/')
def index():
    form = CarForm()
    if form.validate_on_submit():
        flash(f'Request Submitted')
    return render_template('index.jinja', car_form = form, title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        u = User(username=username, email=email, password_hash='', first_name=first_name, last_name=last_name)
        user_match = User.query.filter_by(username=username).first()
        email_match = User.query.filter_by(email=email).first()
        if user_match:
            flash(f'Username {username} already exists, try again.')
            return redirect('/register')
        elif email_match:
            flash(f'Email {email} already exists, try again')    
            return redirect('/register')
        else:
            u.hash_password(password)
            u.commit()
                # db.session.add(u)
                # db.session.commit()
            flash(f'Request to register {username} successful')
            return redirect('/')
    return render_template('register.jinja', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = SignInForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_match = User.query.filter_by(username=username).first()
        if not user_match or not user_match.check_password(password):
            flash(f'Username or Password was incorrect, try again.')
            return redirect('/signin')
        flash(f'{username} succesfully signed in!')
        login_user(user_match)
        return redirect('/')
    return render_template('signin.jinja',sign_in_form=form)

@app.route('/blog')
def blog():
    form = BlogForm()
    return render_template('blog.jinja', blog_form = form)

