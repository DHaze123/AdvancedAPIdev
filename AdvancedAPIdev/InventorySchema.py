from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class InventorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Inventory
        load_instance = True


inventory_schema = InventorySchema()
inventories_schema = InventorySchema(many=True)