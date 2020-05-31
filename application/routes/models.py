from application import db

class Route(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  route_type = db.Column(db.String(100), nullable=False)
  ascents = db.relationship("Ascent", backref='ascent', lazy=True)

  def __init__(self, name, route_type):
    self.name = name
    self.route_type = route_type
