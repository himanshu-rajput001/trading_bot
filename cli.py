import argparse

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_limit_price
)
from bot.logging_config import setup_logger


def main():

    # Start logging
    logger = setup_logger()

    # Create CLI parser
    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol e.g. BTCUSDT"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order side"
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order type"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Required for LIMIT orders"
    )


    # Read user input
    args = parser.parse_args()


    # Validate input
    validate_side(args.side)

    validate_order_type(args.type)

    validate_quantity(args.quantity)

    validate_limit_price(
        args.type,
        args.price
    )


    # Show request summary
    print("\nOrder Request Summary")
    print("--------------------")
    print("Symbol:", args.symbol)
    print("Side:", args.side)
    print("Type:", args.type)
    print("Quantity:", args.quantity)

    if args.price:
        print("Price:", args.price)


    try:

        # Connect Binance
        client = BinanceClient().get_client()

        # Create order manager
        order_manager = OrderManager(client)


        # Place order
        if args.type == "MARKET":

            response = order_manager.place_market_order(
                args.symbol,
                args.side,
                args.quantity
            )

        else:

            response = order_manager.place_limit_order(
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )


        # Print response
        print("\nOrder Response")
        print("----------------")

        print(
            "Order ID:",
            response.get("orderId")
        )

        print(
            "Status:",
            response.get("status")
        )

        print(
            "Executed Quantity:",
            response.get("executedQty")
        )

        print(
            "Average Price:",
            response.get(
                "avgPrice",
                "Not available"
            )
        )


        print(
            "\nOrder placed successfully!"
        )


        logger.info(
            f"Order successful: {response}"
        )


    except Exception as e:

        print("\nOrder failed!")
        print("Error:", e)

        logger.error(
            f"Order failed: {e}"
        )


if __name__ == "__main__":
    main()