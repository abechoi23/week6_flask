from flask import render_template, flash, redirect
from app import app 
from app.forms import RegisterForm, SignInForm, BlogForm

@app.route('/')
def index():
    cdn={
        'instructors':('lucas', 'dylan'),
        'students':['blane','ashmika','abe','zi','connor','martin','noah','erm']
    }
    return render_template('index.jinja', cdn=cdn, title='Home')


@app.route('/about')
def about():
    return render_template('about.jinja')


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit:
        flash(f'Request to register {form.username} successful')
        return redirect('/')
    return render_template('register.jinja', form=form)


@app.route('/signin', methods=['GET','POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit:
        flash(f'{form.username} succesfully signed in!')
        return redirect('/')
    return render_template('signin.jinja', sign_in_form=form)


@app.route('/blog')
def blog():
    form = BlogForm()
    return render_template('blog.jinja', blog_form=form)

