"""Import packages and modules."""
import os
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask import Blueprint
from app.main.forms import NewUserForm, NewMealForm
from app.models import User, Meal, Schedule
from app.extensions import db

main = Blueprint('main', __name__)

# Create your routes here.

@main.route('/')
def homepage():
    return render_template('home.html')

@main.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = NewUserForm()

    if form.validate_on_submit():
        username = form.username.data
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Sorry! Username is already taken.')
            return redirect(url_for('main.create_user'))
        else:
            new_user = User(
                username=form.username.data
            )
            db.session.add(new_user)
            db.session.commit()
            flash(f"Welcome {new_user.username}!")
            return redirect(url_for('main.user'))
    return render_template('create_user.html', form=form)
    

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).one()
    return render_template('user.html', user=user)

@main.route('/meals')
def meals():
    meals = Meal.query.all()

    return render_template('meals.html', meals=meals)

@main.route('/create_meal', methods=['GET', 'POST'])
def create_meal():
    form = NewMealForm()

    if form.validate_on_submit():
        mealname = form.name.data
        existing_meal = Meal.query.filter_by(name=mealname).first()
        if existing_meal:
            flash('Meal already exists.')
            return redirect(url_for('main.create_meal'))
        else:
            new_meal = Meal(
                name=form.name.data,
                ingredients=form.ingredients.data,
                instructions=form.instructions.data
            )
            db.session.add(new_meal)
            db.session.commit()
            flash(f"{new_meal.name} has been added.")
            return redirect(url_for('main.meal_details', meal_id=new_meal.id))
    return render_template('create_meal.html', form=form)

@main.route('/meal/<meal_id>')
def meal_details(meal_id):
    meal = Meal.query.filter_by(id=meal_id).first()

    return render_template('meal_detail.html', meal=meal)



    
