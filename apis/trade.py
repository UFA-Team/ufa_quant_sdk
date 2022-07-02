from apis import _get_request, _post_request
from utils import pprint
from config import API_KEY
TRADE_URL = "http://ufacareer.com/trade/api/"

ROUTE_ACCOUNT_CASH = "account/cash"
def get_cash_avaliable():
    return _post_request(TRADE_URL, ROUTE_ACCOUNT_CASH, {'API_KEY': API_KEY}).json()['data']

ROUTE_ACCOUNT_TOTAL_ASSET = "account/asset_total"
def get_total_asset():
    return _post_request(TRADE_URL, ROUTE_ACCOUNT_TOTAL_ASSET, {'API_KEY': API_KEY}).json()['data']

ROUTE_ACCOUNT_POSITIONS = "account/positions"
def get_positions():
    return _post_request(TRADE_URL, ROUTE_ACCOUNT_POSITIONS, {'API_KEY': API_KEY}).json()['data']

ROUTE_ACCOUNT_ORDERS = "trade/orders"
def get_orders(status="open"):
    return _post_request(TRADE_URL, ROUTE_ACCOUNT_ORDERS, {'API_KEY': API_KEY, 'status': status}).json()['data']

ROUTE_MAKE_ORDER = "trade/make_order"
def make_order(symbol, order_type, side, amount, order_price=None):
    return _post_request(TRADE_URL, ROUTE_MAKE_ORDER, {
        'API_KEY': API_KEY,
        'symbol': symbol,
        'side': side,
        'order_type': order_type,
        'amount': amount,
        'order_price': order_price
    }).json()['data']

if __name__ == '__main__':
    pprint(get_cash_avaliable())
    pprint(get_positions())
    pprint(get_orders())