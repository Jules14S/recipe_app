from flask import request, jsonify, render_template, redirect, url_for
from app import db
from app.models import Recipe, Ingredient, RecipeIngredient
from werkzeug.utils import secure_filename
import os, json
from app.models import Recipe
from flask import current_app 


def init_routes(app):
    @app.route('/')
    def home():
        recipes = Recipe.query.all()
        return render_template('home.html', recipes=recipes)

    @app.route('/recipe/<int:recipe_id>')
    def view_recipe(recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        ingredients = recipe.ingredients
        return render_template('view_recipe.html', recipe=recipe, ingredients=ingredients)

    @app.route('/add', methods=['GET', 'POST'])
    def add_recipe():
        if request.method == 'POST':
            name = request.form['name']
            category = request.form['category']
            instructions = request.form['instructions']
            image = request.files['image']
            image_filename = None

            if image:
                filename = secure_filename(image.filename)
                image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
                image_filename = filename

            recipe = Recipe(name=name, category=category, instructions=instructions, image_filename=image_filename)
            db.session.add(recipe)
            db.session.commit()
            return redirect(url_for('home'))

        return render_template('add_recipe.html')

    @app.route('/recipes', methods=['POST'])
    def create_recipe():
        name = request.form.get('name')
        category = request.form.get('category')
        instructions = request.form.get('instructions')
        ingredients_raw = request.form.get('ingredients')
        ingredients = json.loads(ingredients_raw) if ingredients_raw else []

        image = request.files.get('image')
        image_filename = None
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            image_filename = filename

        recipe = Recipe(name=name, category=category, instructions=instructions, image_filename=image_filename)
        db.session.add(recipe)
        db.session.flush()

        for item in ingredients:
            name = item['name']
            quantity = item['quantity']
            unit = item.get('unit')

            ingredient = Ingredient.query.filter_by(name=name).first()
            if not ingredient:
                ingredient = Ingredient(name=name, unit=unit)
                db.session.add(ingredient)
                db.session.flush()

            assoc = RecipeIngredient(recipe_id=recipe.id, ingredient_id=ingredient.id, quantity=quantity)
            db.session.add(assoc)

        db.session.commit()
        return jsonify({"message": "Recipe created!"}), 201

    @app.route('/recipes', methods=['GET'])
    def list_recipes():
        recipes = Recipe.query.all()
        result = []
        for recipe in recipes:
            result.append({
                "id": recipe.id,
                "name": recipe.name,
                "category": recipe.category,
                "instructions": recipe.instructions
            })
        return jsonify(result), 200

    @app.route('/recipes/<int:recipe_id>/upload-image', methods=['POST'])
    def upload_image(recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)

        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        image = request.files['image']
        if image.filename == '':
            return jsonify({"error": "No selected file"}), 400

        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        print(f"Saved image to {image_path}")



        recipe.image_filename = filename
        db.session.commit()

        return jsonify({"message": f"Image uploaded for recipe {recipe.name}!"}), 200

    @app.route('/recipes/<int:recipe_id>', methods=['GET'])
    def get_recipe(recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        ingredients_data = [{
            "name": ri.ingredient.name,
            "quantity": ri.quantity,
            "unit": ri.ingredient.unit
        } for ri in recipe.ingredients]

        return jsonify({
            "id": recipe.id,
            "name": recipe.name,
            "category": recipe.category,
            "instructions": recipe.instructions,
            "ingredients": ingredients_data,
            "image_url": f"/static/uploads/{recipe.image_filename}" if recipe.image_filename else None
        }), 200

    @app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
    def delete_recipe(recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        RecipeIngredient.query.filter_by(recipe_id=recipe.id).delete()
        db.session.delete(recipe)
        db.session.commit()
        return jsonify({"message": f"Recipe {recipe.name} deleted!"}), 200

    @app.route('/recipes/<int:recipe_id>', methods=['PUT'])
    def update_recipe(recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        data = request.json

        recipe.name = data.get('name', recipe.name)
        recipe.category = data.get('category', recipe.category)
        recipe.instructions = data.get('instructions', recipe.instructions)

        RecipeIngredient.query.filter_by(recipe_id=recipe.id).delete()

        for item in data.get('ingredients', []):
            name = item['name']
            quantity = item['quantity']
            unit = item.get('unit')

            ingredient = Ingredient.query.filter_by(name=name).first()
            if not ingredient:
                ingredient = Ingredient(name=name, unit=unit)
                db.session.add(ingredient)
                db.session.flush()

            assoc = RecipeIngredient(recipe_id=recipe.id, ingredient_id=ingredient.id, quantity=quantity)
            db.session.add(assoc)

        db.session.commit()
        return jsonify({"message": f"Recipe '{recipe.name}' updated!"}), 200
