from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Exynox7510#",
    database="carrent"
)
cursor = db.cursor()

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if user exists in database
    cursor.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()

    if user:
        return redirect(url_for('index'))
    else:
        return "Invalid login credentials"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    message = ""
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        color = request.form['color']
        price = request.form['price']
        cursor.execute("INSERT INTO cars (make, model, year, color, price) VALUES (%s, %s, %s, %s, %s)", (make, model, year, color, price))
        db.commit()
        message = "Car successfully added"
    return render_template('add_car.html', message=message)

@app.route('/available_cars')
def available_cars():
    cursor.execute("SELECT * FROM cars WHERE available = TRUE")
    cars = cursor.fetchall()
    return render_template('available_car.html', cars=cars)

@app.route('/rent/<int:car_id>', methods=['GET', 'POST'])
def rent(car_id):
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        customer_email = request.form['customer_email']
        rental_days = request.form['rental_days']

        cursor.execute("INSERT INTO customer (name, email) VALUES (%s, %s)", (customer_name, customer_email))
        db.commit()
        customer_id = cursor.lastrowid

        cursor.execute("INSERT INTO rental (car_id, customer_id, rental_days) VALUES (%s, %s, %s)", (car_id, customer_id, rental_days))
        db.commit()

        cursor.execute("UPDATE cars SET available = FALSE WHERE id = %s", (car_id,))
        db.commit()

        cursor.execute("SELECT LAST_INSERT_ID()")
        rental_id = cursor.fetchone()[0]

        return f"Car rented successfully. Rental ID: {rental_id}"
    else:
        return render_template('rent.html', car_id=car_id)

@app.route('/return', methods=['GET', 'POST'])
def return_car():
    if request.method == 'POST':
        rental_id = request.form['rental_id']

        cursor.execute("SELECT * FROM rental WHERE id = %s", (rental_id,))
        rental = cursor.fetchone()

        if rental:
            car_id = rental[1]

            cursor.execute("UPDATE cars SET available = TRUE WHERE id = %s", (car_id,))
            db.commit()

            return "Car returned successfully"
        else:
            return "Rental ID not found"
    else:
        return render_template('return.html')

if __name__ == '__main__':
    app.run(debug=True)
