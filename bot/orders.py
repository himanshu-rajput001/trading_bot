import logging

from binance.enums import ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT


class OrderManager:

    def __init__(self, client):
        self.client = client
        self.logger = logging.getLogger("trading_bot")


    def place_market_order(self, symbol, side, quantity):

        try:

            self.logger.info(
                f"Market order request: {symbol}, {side}, {quantity}"
            )

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )

            self.logger.info(
                f"Market order response: {order}"
            )

            return order


        except Exception as e:

            self.logger.error(
                f"Market order failed: {e}"
            )

            raise


    def place_limit_order(self, symbol, side, quantity, price):

        try:

            self.logger.info(
                f"Limit order request: {symbol}, {side}, {quantity}, price={price}"
            )

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )

            self.logger.info(
                f"Limit order response: {order}"
            )

            return order


        except Exception as e:

            self.logger.error(
                f"Limit order failed: {e}"
            )

            raise