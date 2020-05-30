from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators

class RouteForm(FlaskForm):
  name = StringField("Route name", [validators.InputRequired(), validators.length(min=1, max=50)])
  route_type = SelectField('Type of route', 
  [validators.AnyOf(['boulder', 'sport', 'traditional'])],
  choices=[('boulder', 'Boulder'), ('sport', 'Sport/Bolted'), ('traditional', 'Traditional')])
  class Meta:
    csrf = False

class UpdateRouteForm(FlaskForm):
  new_name = StringField('New name', [validators.InputRequired(), validators.length(min=1, max=50)])
  class Meta:
    csrf = False