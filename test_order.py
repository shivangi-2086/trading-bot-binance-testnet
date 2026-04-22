from orders import place_market_order, place_limit_order

print("MARKET ORDER RESPONSE")
market = place_market_order(
    symbol="BTCUSDT",
    side="BUY",
    quantity=0.001,
    mock=True
)
print(market)

print("\nLIMIT ORDER RESPONSE")
limit = place_limit_order(
    symbol="BTCUSDT",
    side="SELL",
    quantity=0.001,
    price=30000,
    mock=True
)
print(limit)