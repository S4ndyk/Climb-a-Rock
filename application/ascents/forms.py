from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, HiddenField,validators

grades = [
  '4', '5', '5+', 
  '6a', '6a+', '6b', '6b+', '6c', '6c+', 
  '7a', '7a+', '7b', '7b+', '7c', '7c+'
  ]


class AscentForm(FlaskForm):
  grade = SelectField('Grade estimaet', choices=grades)
  route_id = HiddenField('Route')
  user_id = HiddenField('User')
  class Meta:
    csrf = False