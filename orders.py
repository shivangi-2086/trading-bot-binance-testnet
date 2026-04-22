import logging
from client import client

def place_market_order(symbol, side, quantity, mock=False):
    if mock:
        logging.info("MOCK MODE ENABLED - MARKET")
        return {
            "orderId": 123456789,
            "symbol": symbol,
            "status": "FILLED",
            "executedQty": quantity,
            "side": side,
            "avgPrice": "TESTNET"
        }

    try:
        return client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
    except Exception as e:
        logging.error(f"Market order failed: {e}")
        raise


def place_limit_order(symbol, side, quantity, price, mock=False):
    if mock:
        logging.info("MOCK MODE ENABLED - LIMIT")
        return {
            "orderId": 987654321,
            "symbol": symbol,
            "status": "NEW",
            "price": price,
            "quantity": quantity,
            "side": side
        }

    try:
        return client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
    except Exception as e:
        logging.error(f"Limit order failed: {e}")
        raise