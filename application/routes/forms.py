from flask_wtf import FlaskForm
from wtforms import StringField, SelectField

class RouteForm(FlaskForm):
  name = StringField("Route name")
  route_type = SelectField('Type of route', choices=[(
      'boulder', 'Boulder'), ('sport', 'Sport/Bolted'), ('traditional', 'Traditional')])
  class Meta:
    csrf = False

class UpdateRouteForm(FlaskForm):
  new_name = StringField('New name')
  class Meta:
    csrf = False