@customer_bp.route("/my-tickets", methods=["GET"])
@token_required
def my_tickets(customer_id):

    tickets = ServiceTicket.query.filter_by(
        customer_id=customer_id
    ).all()

    return service_ticket_schema.jsonify(
        tickets,
        many=True
    )