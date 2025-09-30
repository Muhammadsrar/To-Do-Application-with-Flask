from functools import wraps
from flask import request, jsonify
import jwt
from models.user import User

SECRET_KEY = "your_secret_key_here"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None  

        #  Try to get token from cookie
        if "token" in request.cookies:
            token = request.cookies.get("token")

        #  If token still missing
        if not token:
            return jsonify({"error": "Token missing"}), 401

        try:
            # Decode JWT token
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = User.objects(id=data["user_id"]).first()
            if not current_user:
                return jsonify({"error": "User not found"}), 401

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        #  Return user to the route
        return f(current_user, *args, **kwargs)

    return decorated
