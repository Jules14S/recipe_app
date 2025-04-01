from flask_sqlalchemy import SQLAlchemy
from app import db


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=True)
    instructions = db.Column(db.Text, nullable=True)
    image_filename = db.Column(db.String(255), nullable=True)

    ingredients = db.relationship('RecipeIngredient', back_populates='recipe')




class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    unit = db.Column(db.String(20))
    calories = db.Column(db.Float)
    
    recipes = db.relationship('RecipeIngredient', back_populates='ingredient')


class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    quantity = db.Column(db.Float)

    recipe = db.relationship('Recipe', back_populates='ingredients')
    ingredient = db.relationship('Ingredient', back_populates='recipes')
