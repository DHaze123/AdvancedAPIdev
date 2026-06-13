@ticket_bp.route("/<int:ticket_id>/edit", methods=["PUT"])
def edit_ticket(ticket_id):

    ticket = ServiceTicket.query.get_or_404(ticket_id)

    data = request.json

    add_ids = data.get("add_ids", [])
    remove_ids = data.get("remove_ids", [])

    for mechanic_id in add_ids:

        mechanic = Mechanic.query.get(mechanic_id)

        if mechanic and mechanic not in ticket.mechanics:
            ticket.mechanics.append(mechanic)

    for mechanic_id in remove_ids:

        mechanic = Mechanic.query.get(mechanic_id)

        if mechanic and mechanic in ticket.mechanics:
            ticket.mechanics.remove(mechanic)

    db.session.commit()

    return jsonify({
        "message": "Ticket updated"
    })