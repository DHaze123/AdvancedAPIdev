@ticket_bp.route(
    "/<int:ticket_id>/add-part/<int:part_id>",
    methods=["POST"]
)
def add_part(ticket_id, part_id):

    ticket = ServiceTicket.query.get_or_404(ticket_id)

    part = Inventory.query.get_or_404(part_id)

    ticket.parts.append(part)

    db.session.commit()

    return jsonify({
        "message": "Part added to ticket"
    })