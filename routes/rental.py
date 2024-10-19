# routes/rental.py
from flask import Blueprint, render_template, request
from database import get_db_connection

rental_bp = Blueprint('rental', __name__)

@rental_bp.route('/rent/<int:car_id>', methods=['GET', 'POST'])
def rent(car_id):
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        customer_email = request.form['customer_email']
        rental_days = request.form['rental_days']

        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO customer (name, email) VALUES (%s, %s)", (customer_name, customer_email))
        db.commit()
        customer_id = cursor.lastrowid

        cursor.execute("INSERT INTO rental (car_id, customer_id, rental_days) VALUES (%s, %s, %s)", (car_id, customer_id, rental_days))
        db.commit()

        cursor.execute("UPDATE cars SET available = FALSE WHERE id = %s", (car_id,))
        db.commit()

        cursor.execute("SELECT LAST_INSERT_ID()")
        rental_id = cursor.fetchone()[0]

        cursor.close()
        db.close()

        return f"Car rented successfully. Rental ID: {rental_id}"
    else:
        return render_template('rent.html', car_id=car_id)

@rental_bp.route('/return', methods=['GET', 'POST'])
def return_car():
    if request.method == 'POST':
        rental_id = request.form['rental_id']

        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM rental WHERE id = %s", (rental_id,))
        rental = cursor.fetchone()

        if rental:
            car_id = rental[1]
            cursor.execute("UPDATE cars SET available = TRUE WHERE id = %s", (car_id,))
            db.commit()
            cursor.close()
            db.close()
            return "Car returned successfully"
        else:
            cursor.close()
            db.close()
            return "Rental ID not found"
    else:
        return render_template('return.html')
