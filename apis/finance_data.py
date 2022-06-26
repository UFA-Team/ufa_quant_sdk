from apis import _get_request, _post_request
# FINANCE_URL = "http://ufacareer.com/finance/api/"
FINANCE_URL = "http://192.168.31.210:10987/api/"

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
    from pprint import pprint
    # pprint(get_symbol_list())

    # pprint(get_index_list())

    pprint(get_kline("SZ.000001", "20220301", "20220310"))
