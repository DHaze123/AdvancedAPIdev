from jose import jwt
from functools import wraps
from flask import request, jsonify

SECRET_KEY = "super-secret-key"

def encode_token(customer_id):
    payload = {
        "customer_id": customer_id
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        auth = request.headers.get("Authorization")

        if not auth:
            return jsonify({"error": "Token missing"}), 401

        token = auth.split(" ")[1]

        try:
            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=["HS256"]
            )

            customer_id = payload["customer_id"]

        except:
            return jsonify({"error": "Invalid token"}), 401

        return f(customer_id, *args, **kwargs)

    return decorated