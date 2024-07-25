# run.py
from app import create_app, db
from app.models.user import User

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables for our data models
    app.run(debug=True)