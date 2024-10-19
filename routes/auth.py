# routes/auth.py
from flask import Blueprint, render_template, request, redirect, url_for
from database import get_db_connection

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def login_page():
    return render_template('login.html')

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    db.close()

    if user:
        return redirect(url_for('index'))
    else:
        return "Invalid login credentials"
