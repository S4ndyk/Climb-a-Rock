from application import db

class Ascent(db.Model):
  grade = db.Column(db.String(10), nullable=True)
  send_date = db.Column(db.DateTime, default=db.func.current_timestamp())
  account_id = db.Column(db.Integer, db.ForeignKey('account.id'), primary_key=True, nullable=False)
  route_id = db.Column(db.Integer, db.ForeignKey('route.id'), primary_key=True, nullable=False)
  
  def __init__(self, grade, route_id, account_id):
    self.grade = grade
    self.route_id = route_id
    self.account_id = account_id
    self.account_id = account_id