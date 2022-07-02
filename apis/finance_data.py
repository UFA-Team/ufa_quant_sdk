from apis import _get_request, _post_request
from utils import pprint
FINANCE_URL = "http://ufacareer.com/finance/api/"

ROUTE_SYMBOL_LIST = "general/symbols"
def get_symbol_list():
    return _get_request(FINANCE_URL, ROUTE_SYMBOL_LIST, {'type': 'a'}).json()['data']

ROUTE_INDEX_LIST = "general/indexs"
def get_index_list():
    return _get_request(FINANCE_URL, ROUTE_INDEX_LIST, {'type': 'a'}).json()['data']

ROUTE_KLINE = "hist/kline"
def get_kline(symbol, start, end, tf='1d'):
    payload = {
        "symbol": symbol,
        "start": start,
        "end": end,
        "tf": tf
    }
    return _post_request(FINANCE_URL, ROUTE_KLINE, payload).json()['data']


if __name__ == '__main__':
    pprint(get_kline("SZ.000001", "2022-03-01 00:00:00", "2022-03-10 00:00:00"))
