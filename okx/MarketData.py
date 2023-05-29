from .client import Client
from .consts import *


class MarketAPI(Client):

    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1',
                 domain='https://www.okx.com', debug=True):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain, debug)

    # Get Tickers
    def get_tickers(self, inst_type, uly='', inst_family=''):
        if uly:
            params = {'instType': inst_type, 'uly': uly, 'instFamily': inst_family}
        else:
            params = {'instType': inst_type, 'instFamily': inst_family}
        return self._request_with_params(GET, MARKET_TICKERS_INFO, params)

    # Get Ticker
    def get_ticker(self, inst_id):
        params = {'instId': inst_id}
        return self._request_with_params(GET, MARKET_TICKER_INFO, params)

    # Get Index Tickers
    def get_index_tickers(self, quote_ccy='', inst_id=''):
        params = {'quoteCcy': quote_ccy, 'instId': inst_id}
        return self._request_with_params(GET, MARKET_INDEX_TICKERS, params)

    # Get Order Book
    def get_orderbook(self, inst_id, sz=''):
        params = {'instId': inst_id, 'sz': sz}
        return self._request_with_params(GET, MARKET_ORDER_BOOKS, params)

    # Get Candlesticks
    def get_candlesticks(self, inst_id, after='', before='', bar='', limit=''):
        params = {'instId': inst_id, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request_with_params(GET, MARKET_MARKET_CANDLES, params)

    # GGet Candlesticks History（top currencies only）
    def get_history_candlesticks(self, inst_id, after='', before='', bar='', limit=''):
        params = {'instId': inst_id, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request_with_params(GET, MARKET_HISTORY_CANDLES, params)

    # Get Index Candlesticks
    def get_index_candlesticks(self, inst_id, after='', before='', bar='', limit=''):
        params = {'instId': inst_id, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request_with_params(GET, MARKET_INDEX_CANSLES, params)

    # Get Mark Price Candlesticks
    def get_mark_price_candlesticks(self, inst_id, after='', before='', bar='', limit=''):
        params = {'instId': inst_id, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request_with_params(GET, MARKET_MARKPRICE_CANDLES, params)

    # Get Index Candlesticks
    def get_trades(self, inst_id, limit=''):
        params = {'instId': inst_id, 'limit': limit}
        return self._request_with_params(GET, MARKET_TRADES, params)

    # Get Volume
    def get_volume(self):
        return self._request_without_params(GET, MARKET_24_VOLUMNE)

    # Get Oracle
    def get_open_oracle(self):
        return self._request_without_params(GET, MARKET_OPEN_ORACLE)

    # Get Tier
    def get_tier(self, inst_type='', td_mode='', uly='', inst_id='', ccy='', tier=''):
        params = {'instType': inst_type, 'tdMode': td_mode, 'uly': uly, 'instId': inst_id, 'ccy': ccy, 'tier': tier}
        return self._request_with_params(GET, TIER, params)

    # GET /api/v5/market/index-components
    def get_index_components(self, index=''):
        param = {
            'index': index
        }
        return self._request_with_params(GET, MARKET_INDEX_COMPONENTS, param)

    # GET /api/v5/market/exchange-rate
    def get_exchange_rate(self):
        return self._request_without_params(GET, MARKET_EXCHANGE_RATE)

    # GET /api/v5/market/history-trades
    def get_history_trades(self, inst_id='', type='', after='', before='', limit=''):
        params = {
            'instId': inst_id,
            'type': type,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request_with_params(GET, MARKET_HISTORY_TRADES, params)

    # GET /api/v5/market/block-ticker
    def get_block_ticker(self, inst_id=''):
        params = {
            'instId': inst_id
        }
        return self._request_with_params(GET, MARKET_BLOCK_TICKER, params)

    # GET /api/v5/market/block-tickers
    def get_block_tickers(self, inst_type='', uly='', inst_family=''):
        params = {
            'instType': inst_type,
            'uly': uly,
            'instFamily': inst_family
        }
        return self._request_with_params(GET, MARKET_BLOCK_TICKERS, params)

    # GET /api/v5/market/block-trades
    def get_block_trades(self, inst_id=''):
        params = {
            'instId': inst_id
        }
        return self._request_with_params(GET, MARKET_BLOCK_TRADES, params)
