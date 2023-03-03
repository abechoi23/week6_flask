from . import bp as social_bp
# from auth import bp as auth_bp
from flask import render_template, flash, redirect
from .forms import BlogForm
from .models import User, Post, Car
from flask_login import current_user, login_required


@social_bp.route('/user/<username>')  #add in specific user use <> 
@login_required
def user(username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        return redirect('/')
    posts = user_match.posts
    cars = user_match.cars
    return render_template('user.jinja', user=user_match,posts=posts, cars=cars)


@social_bp.route('/blog', methods=['GET','POST'])
def blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        user_id = current_user.id
        p = Post(title=title, body=body, user_id=user_id)
        flash(f'{title} succesfully posted!')
        p.commit()
        # db.session.add(u)
        # db.session.commit()
    return render_template('blog.jinja', blog_form=form)

