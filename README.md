# Recipe & Ingredient Manager

A full-stack web application built with Flask and MySQL that includes a user-friendly web interface for managing recipes and ingredients. Users can add, edit, delete, and view recipes along with their instructions, ingredients, and images.

## Features

- Add, update, and delete recipes via a responsive web interface  
- Attach images to recipes (uploaded and displayed)  
- Manage individual ingredients per recipe  
- Full CRUD functionality with persistent MySQL database  
- REST API endpoints available for programmatic access

## Technologies Used

- Python (Flask)  
- MySQL, SQLAlchemy  
- HTML, CSS (Bootstrap)  
- JavaScript  
- Jinja2 templating engine

## Frontend

The application includes a full HTML/CSS interface built with Flask’s Jinja2 templates and styled with Bootstrap.

-  Browse all recipes from the homepage  
-  View individual recipes with ingredients and instructions  
-  Add new recipes via a form (with image upload support)  
-  Images are uploaded and rendered directly in the app

## Getting Started

### Prerequisites

- Python 3.x  
- MySQL  
- Required Python packages:
  ```bash
  pip install -r requirements.txt
  ```

### Database Setup

1. Create a `.env` file in the root directory with the following content:

    ```
    MYSQL_USER=your_mysql_user
    MYSQL_PASSWORD=your_mysql_password
    MYSQL_HOST=localhost
    MYSQL_PORT=3306
    MYSQL_DB=recipe_app
    ```

2. Create the database in MySQL:

    ```sql
    CREATE DATABASE recipe_app;
    ```

### Run the App

```bash
python run.py
```

Then open your browser to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## API Endpoints

- `GET /recipes` – List all recipes (JSON)  
- `POST /recipes` – Add a recipe with ingredients  
- `PUT /recipes/<id>` – Update a recipe  
- `DELETE /recipes/<id>` – Delete a recipe  
- `POST /recipes/<id>/upload-image` – Upload image to a recipe

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

