from extension import db

class Account(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  type = db.Column(db.String(120), nullable=False)
  balance = db.Column(db.Float, nullable=False)
  credit_limit = db.Column(db.Float, nullable=True)
  created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
  updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

  user = db.relationship('User', backref='accounts')
