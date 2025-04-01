import os
os.chdir(os.path.dirname(__file__))

from app import create_app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

