from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField


class BlogForm(FlaskForm):
    title = StringField('Title')
    body = TextAreaField('Body')
    submit = SubmitField('Submit')
