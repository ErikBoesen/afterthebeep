from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    content = TextAreaField('Write here.', validators=[DataRequired()])
