import cbpro
import time
import logging
from sortedcontainers import SortedDict

class OrderBookCustom(cbpro.OrderBook):
    def __init__(self, product_id='BTC-USD', auth_client=None):
        self.logger = logging.getLogger('trader-logger')
        self.error_logger = logging.getLogger('error-logger')
        super(OrderBookCustom, self).__init__(product_id=product_id)
        if auth_client is not None:
            self._client = auth_client

    def is_ready(self):
        try:
            super(OrderBookCustom, self).get_ask()
        except (ValueError, AttributeError):
            return False
        return True

    def get_ask(self):
        while not self.is_ready():
            time.sleep(0.01)
        return super(OrderBookCustom, self).get_ask()

    def get_bid(self):
        while not self.is_ready():
            time.sleep(0.01)
        return super(OrderBookCustom, self).get_bid()

    def reset_book(self):
        self._asks = SortedDict()
        self._bids = SortedDict()
        res = self._client.get_product_order_book(product_id=self.product_id, level=3)
        if 'bids' not in res:
            return
        for bid in res['bids']:
            self.add({
                'id': bid[2],
                'side': 'buy',
                'price': Decimal(bid[0]),
                'size': Decimal(bid[1])
            })
        for ask in res['asks']:
            self.add({
                'id': ask[2],
                'side': 'sell',
                'price': Decimal(ask[0]),
                'size': Decimal(ask[1])
            })
        self._sequence = res['sequence']
