# Recipe & Ingredient Manager

A full-stack web app built with Flask and MySQL to manage recipes and their ingredients.
Users can view, add, and delete recipes, as well as upload a picture of the dish.

## Features

- Add, update, and delete recipes
- Attach images to recipes
- Manage ingredients per recipe
- Responsive UI with Bootstrap
- REST API endpoints

## Technologies Used

- Python (Flask)
- MySQL
- SQLAlchemy
- HTML, CSS (Bootstrap)
- JavaScript

## Getting Started

### Prerequisites

- Python 3.x
- MySQL
- `pip install -r requirements.txt`

### Database Setup

Create a `.env` file in the root directory with the following variables:

```
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=recipe_app
```

Create the database in MySQL Workbench or the CLI:

```sql
CREATE DATABASE recipe_app;
```

### Run the App

```bash
python run.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## API Endpoints

- `GET /recipes` – List all recipes
- `POST /recipes` – Add a recipe with ingredients
- `PUT /recipes/<id>` – Update a recipe
- `DELETE /recipes/<id>` – Delete a recipe
- `POST /recipes/<id>/upload-image` – Upload image for a recipe

## Folder Structure

```
restructured_recipe_app/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── add_recipe.html
│   │   ├── view_recipe.html
│   │   └── layout.html
├── static/
│   └── uploads/
├── .env
├── run.py
└── README.md
```

## License

This project is for educational purposes and not production-ready. Feel free to build on it!
