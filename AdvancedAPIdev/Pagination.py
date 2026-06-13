@customer_bp.route("/")
def get_customers():

    page = request.args.get(
        "page",
        1,
        type=int
    )

    per_page = request.args.get(
        "per_page",
        5,
        type=int
    )

    customers = Customer.query.paginate(
        page=page,
        per_page=per_page
    )

    return jsonify({
        "customers": customer_schema.dump(
            customers.items,
            many=True
        ),
        "total": customers.total,
        "pages": customers.pages
    })