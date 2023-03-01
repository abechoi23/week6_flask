from flask import render_template, flash, redirect 
from app import app
from app.forms import RegisterForm, SignInForm, CarForm
# from app.forms import RegisterForm

@app.route('/')
def index():
    form = CarForm()
    if form.validate_on_submit:
        flash(f'Request Submitted')
    return render_template('index.jinja', car_form = form, title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit:
        flash(f'Request to register {form.username} successful')
    return render_template('register.jinja', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = SignInForm()
    if form.validate_on_submit:
        flash(f'{form.username} succesfully signed in!')
    return render_template('login.jinja', sign_in_form=form)

@app.route('/blog')
def blog():
    return render_template('blog.jinja')

