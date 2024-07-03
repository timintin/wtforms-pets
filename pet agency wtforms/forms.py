from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, URL, Optional, NumberRange

class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators=[DataRequired()])
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[DataRequired()])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField('Notes', validators=[Optional()])

class EditPetForm(FlaskForm):
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = TextAreaField('Notes', validators=[Optional()])
    available = BooleanField('Available')