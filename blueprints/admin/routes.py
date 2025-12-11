from flask import render_template, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from . import bp
from extensions import db
from models import User, Car
from decorators import admin_required

@bp.route('/')
@admin_required
def panel():
    users = User.query.order_by(User.created_at.desc()).all()
    cars = Car.query.order_by(Car.created_at.desc()).all()
    return render_template('admin/panel.html', users=users, cars=cars)

@bp.route('/users/<int:user_id>/delete', methods=['POST'])
@admin_required
def delete_user(user_id):
    u = User.query.get_or_404(user_id)
    if u.role == 'admin':
        flash('Нельзя удалить администратора.', 'warning')
    else:
        try:
            db.session.delete(u)
            db.session.commit()
            flash('Пользователь удалён.', 'info')
        except IntegrityError:
            db.session.rollback()
            flash('Невозможно удалить пользователя: есть связанные записи.', 'error')
    return redirect(url_for('admin.panel'))

@bp.route('/cars/<int:car_id>/delete', methods=['POST'])
@admin_required
def delete_car(car_id):
    c = Car.query.get_or_404(car_id)
    try:
        db.session.delete(c)
        db.session.commit()
        flash('Машина удалена.', 'info')
    except IntegrityError:
        db.session.rollback()
        flash('Невозможно удалить машину: есть связанные записи.', 'error')
    return redirect(url_for('admin.panel'))
