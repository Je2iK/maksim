from app import create_app
from extensions import db
from models import User
import os

app = create_app()

with app.app_context():
    # Создаем админа
    email = "admin@dealer.com"
    password = "admin123"
    
    if not User.query.filter_by(email=email.lower()).first():
        u = User(
            email=email.lower(),
            role="admin",
            last_name="Администратор",
            first_name="Админ",
            middle_name=None,
        )
        u.set_password(password)
        db.session.add(u)
        db.session.commit()
        print(f"Создан админ: {email} / {password}")
    else:
        print("Админ уже существует")
