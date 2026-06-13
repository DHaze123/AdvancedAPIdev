from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

service_mechanic = db.Table(
    "service_mechanic",
    db.Column("service_ticket_id", db.Integer, db.ForeignKey("service_ticket.id")),
    db.Column("mechanic_id", db.Integer, db.ForeignKey("mechanic.id"))
)

ticket_inventory = db.Table(
    "ticket_inventory",
    db.Column("service_ticket_id", db.Integer, db.ForeignKey("service_ticket.id")),
    db.Column("inventory_id", db.Integer, db.ForeignKey("inventory.id"))
)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))

    tickets = db.relationship("ServiceTicket", backref="customer")


class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    tickets = db.relationship(
        "ServiceTicket",
        secondary=service_mechanic,
        back_populates="mechanics"
    )


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)

    tickets = db.relationship(
        "ServiceTicket",
        secondary=ticket_inventory,
        back_populates="parts"
    )


class ServiceTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customer.id")
    )

    mechanics = db.relationship(
        "Mechanic",
        secondary=service_mechanic,
        back_populates="tickets"
    )

    parts = db.relationship(
        "Inventory",
        secondary=ticket_inventory,
        back_populates="tickets"
    )