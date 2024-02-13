# Create your forms here.
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, TextAreaField
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError

class NewUserForm(FlaskForm):
    """Form to create new user"""
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=3, max=80, message="Your username must have 3-80 chars.")
                                       ])
    submit = SubmitField('Submit')

class NewMealForm(FlaskForm):
    """Form to create new meal"""
    name = StringField('Name', validators=[DataRequired(),Length(min=3, max=80, message="Your meal name must have 3-80 chars.")])
    ingredients = TextAreaField('Ingredients', [DataRequired()])
    instructions = TextAreaField('Instructions', [DataRequired()])
    submit = SubmitField('Submit')
