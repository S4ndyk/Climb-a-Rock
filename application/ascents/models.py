from application import db

class Ascent(db.Model):
  grade = db.Column(db.String(10), nullable=True)
  account_id = db.Column(db.Integer, db.ForeignKey('account.id'), primary_key=True, nullable=False)
  route_id = db.Column(db.Integer, db.ForeignKey('route.id'), primary_key=True, nullable=False)
  
  def __init__(self, grade):
    self.grade = grade