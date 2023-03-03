from . import bp as main_bp
# from auth import bp as auth_bp
from flask import render_template, flash, redirect
from .forms import CarForm
from flask_login import current_user
from app.blueprints.social.models import Car



@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = CarForm()
    if form.validate_on_submit():
        make = form.make.data
        model = form.model.data
        year = form.year.data
        color = form.color.data
        price = form.price.data
        user_id = current_user.id
        c = Car(make=make, model=model, year=year,
                color=color, price=price, user_id=user_id)
        c.commit()
        flash(f'Request Submitted')
        return redirect('/')
    return render_template('index.jinja', car_form=form, title='Home')


@main_bp.route('/about')
def about():
    return render_template('about.jinja')

