from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField,URLField
from wtforms.validators import InputRequired, NumberRange, AnyOf




class AddPetForm (FlaskForm):
    """ form for adding a pet"""

    name = StringField("Pet Name")
    species = StringField("Species", validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'], message="Species must be either 'cat,' 'dog,' or 'porcupine.'")])
    photo_url = URLField('Website URL')
    age = FloatField("Age", validators=[InputRequired(), NumberRange(min=0, max=30, message="Age must be between 0 and 30.")])
    notes = StringField("Any Notes")

class EditPetForm(FlaskForm):
    """ Form for editing a pet """
    name = StringField("Pet Name")
    species = StringField("Species", validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'], message="Species must be either 'cat,' 'dog,' or 'porcupine.'")])
    photo_url = URLField('Website URL')
    age = FloatField("Age", validators=[InputRequired(), NumberRange(min=0, max=30, message="Age must be between 0 and 30.")])
    notes = StringField("Any Notes")