# app.py
from flask import Flask, render_template
from routes.auth import auth_bp
from routes.car import car_bp
from routes.rental import rental_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(car_bp)
app.register_blueprint(rental_bp)

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
