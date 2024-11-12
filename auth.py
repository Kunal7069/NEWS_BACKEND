from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os
import jwt
import base64
import datetime
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
CORS(app)  
app.config['SECRET_KEY'] = 'INVESTZ123'  # Replace with your actual secret key
port = 7000
# MongoDB connection URI
mongo_uri = "mongodb+srv://TEST:12345@mubustest.yfyj3.mongodb.net/investz?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
db = client["investz"]
user_collection = db["USER"]

# Route to enter data into the USER collection
@app.route('/signup', methods=['POST'])
def add_user():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    contact = request.form.get("contact")
    email = request.form.get("email")
    password = request.form.get("password")
    print(first_name,last_name,contact,email,password)
    # Handling profile photo
    profile_photo = request.files.get("profile_photo")
    photo_data = profile_photo.read() if profile_photo else None
    
    # Hash the password before storing it
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "contact": contact,
        "email": email,
        "password": hashed_password,
        "profile_photo": photo_data
    }

    user_collection.insert_one(user_data)
    return jsonify({"message": "User added successfully"}), 201

# Route for user login and JWT generation
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    
    # Find user by email
    user = user_collection.find_one({"email": email})
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    # Check if password matches
    if not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Generate JWT token
    token = jwt.encode({
        'email': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm="HS256")
    
    # Convert profile photo to Base64 if it exists
    profile_photo_base64 = None
    if user.get('profile_photo'):
        profile_photo_base64 = base64.b64encode(user['profile_photo']).decode('utf-8')
    
    # Return user details along with the token
    user_data = {
        "first_name": user['first_name'],
        "last_name": user['last_name'],
        "contact": user['contact'],
        "email": user['email'],
        "profile_photo": profile_photo_base64,
        "token": token
    }
    return jsonify(user_data), 200

# Decorator to verify the JWT token
def token_required(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Token is missing"}), 403
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 403
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 403
        return f(*args, **kwargs)
    return wrapper

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
