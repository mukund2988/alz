from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from pymongo import MongoClient
import bcrypt
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set the secret key for session management
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# MongoDB connection setup
client = MongoClient(os.getenv('MONGO_URI'))
db = client['Alzh_detection']
collection = db['users']

def add_user(name, username, password, email):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    user_data = {
        "name": name,
        "username": username,
        "password": hashed_password,
        "email": email
    }
    collection.insert_one(user_data)
    return "User added successfully"

def verify_user(username, password):
    user = collection.find_one({"username": username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        return True
    return False

@app.route('/')
def index():
    return render_template('index.html')  # Registration page

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    name = data.get('name')
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    try:
        message = add_user(name, username, password, email)
        return jsonify({'message': message}), 200
    except Exception as e:
        return jsonify({'message': 'Error adding user', 'error': str(e)}), 500

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'GET':
        return render_template('login.html')
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if verify_user(username, password):
        session['username'] = username
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/detection')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect(url_for('login_user'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login_user'))

if __name__ == '__main__':
    app.run(debug=True)
