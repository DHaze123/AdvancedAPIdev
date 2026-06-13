@mechanic_bp.route("/top-mechanics")
def top_mechanics():

    mechanics = Mechanic.query.all()

    sorted_mechanics = sorted(
        mechanics,
        key=lambda m: len(m.tickets),
        reverse=True
    )

    return mechanic_schema.jsonify(
        sorted_mechanics,
        many=True
    )