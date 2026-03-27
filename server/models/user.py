from extensions import db
from passlib.hash import bcrypt

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=False)
  created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
  updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

  def set_password(self, password):
    self.password = bcrypt.generate_password_hash(password).decode('utf-8')

  def check_password(self, password):
    return bcrypt.check_password_hash(self.password, password)
