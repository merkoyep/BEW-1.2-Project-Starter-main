# Create your models here.
from app.extensions import db
from sqlalchemy.orm import backref

class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    schedule = db.relationship('Schedule', back_populates='user')
    
    def __str__(self):
        return f'<User: {self.username}>'

    def __repr__(self):
        return f'<User: {self.username}>'

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.String(80), nullable=False)
    day = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'))

    user = db.relationship('User', back_populates='schedule')

    def __str__(self):
        return f'<Schedule: {self.week}>'

    def __repr__(self):
        return f'<Schedule: {self.week}>'

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ingredients = db.Column(db.Text(), nullable=False)
    instructions = db.Column(db.Text(), nullable=False)

    def __str__(self):
        return f'<Meal: {self.name}>'

    def __repr__(self):
        return f'<Meal: {self.name}>'

