#
# test_period.py
# Mike Cardillo
#
# Pytest tests on the period file

import period
import trade
import datetime
import numpy as np


class TestPeriod(object):
    def setup_class(self):
        self.start_time = datetime.datetime.now(datetime.timezone.utc)
        self.fake_hist_data = [[self.start_time.timestamp(), 123.4, 133.5, 124.6, 132.3, 3485.38],
                               [(self.start_time + datetime.timedelta(minutes=5)).timestamp(), 122.3, 135.4, 123.7, 133.4, 4385.25],
                               [(self.start_time + datetime.timedelta(minutes=10)).timestamp(), 120.2, 130.2, 132.5, 131.2, 3859.42]]

    def test_init__initalize_false(self):
        test_period = period.Period(period_size=15, name="BTC15", product="BTC-USD", initialize=False)

        assert isinstance(test_period, period.Period)
        assert test_period.period_size == 15
        assert test_period.name == "BTC15"
        assert test_period.product == "BTC-USD"
        assert test_period.verbose_heartbeat is False
        assert isinstance(test_period.candlesticks, type(np.array([])))
        np.testing.assert_array_equal(test_period.candlesticks, np.array([]))

    def test_init__initalize_true(self, mocker):
        mocker.patch("cbpro.PublicClient.get_product_historic_rates", return_value=self.fake_hist_data)
        test_period = period.Period(period_size=5, name="ETH5", product="ETH-USD", initialize=True)

        assert isinstance(test_period, period.Period)
        assert test_period.period_size == 5
        assert test_period.name == "ETH5"
        assert test_period.product == "ETH-USD"
        assert test_period.verbose_heartbeat is False

        assert isinstance(test_period.candlesticks, type(np.array([])))
        assert len(test_period.candlesticks) == len(self.fake_hist_data) - 1
        assert isinstance(test_period.curr_candlestick, period.Candlestick)
        assert test_period.curr_candlestick_start == self.start_time
        assert isinstance(test_period.candlesticks[0], type(np.array([])))
