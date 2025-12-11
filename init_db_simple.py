from app import create_app
from extensions import db

app = create_app()

with app.app_context():
    # Создаем все таблицы
    db.create_all()
    print("База данных инициализирована!")
