@customer_bp.route("/login", methods=["POST"])
def login():

    data = request.json

    customer = Customer.query.filter_by(
        email=data["email"]
    ).first()

    if not customer:
        return jsonify({"message": "Invalid credentials"}), 401

    if customer.password != data["password"]:
        return jsonify({"message": "Invalid credentials"}), 401

    token = encode_token(customer.id)

    return jsonify({
        "token": token
    }), 200