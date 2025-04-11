from settings import app, db
from models.form import Form

def generate_models():
    with app.app_context():
        db.create_all()