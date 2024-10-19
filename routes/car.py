# routes/car.py
from flask import Blueprint, render_template, request
from database import get_db_connection

car_bp = Blueprint('car', __name__)

@car_bp.route('/add_car', methods=['GET', 'POST'])
def add_car():
    message = ""
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        color = request.form['color']
        price = request.form['price']

        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO cars (make, model, year, color, price) VALUES (%s, %s, %s, %s, %s)", (make, model, year, color, price))
        db.commit()
        message = "Car successfully added"
        cursor.close()
        db.close()
    return render_template('add_car.html', message=message)

@car_bp.route('/available_cars')
def available_cars():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cars WHERE available = TRUE")
    cars = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('available_car.html', cars=cars)
