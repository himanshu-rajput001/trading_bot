def validate_side(side):
    allowed = ["BUY", "SELL"]

    if side not in allowed:
        raise ValueError(
            "Side must be BUY or SELL"
        )


def validate_order_type(order_type):
    allowed = ["MARKET", "LIMIT"]

    if order_type not in allowed:
        raise ValueError(
            "Order type must be MARKET or LIMIT"
        )


def validate_quantity(quantity):

    if quantity <= 0:
        raise ValueError(
            "Quantity must be greater than zero"
        )


def validate_limit_price(order_type, price):

    if order_type == "LIMIT" and price is None:
        raise ValueError(
            "Price is required for LIMIT order"
        )