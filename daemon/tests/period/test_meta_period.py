#
# test_period.py
# Mike Cardillo
#
# Pytest tests on the period file

import period
import trade
import datetime
import numpy as np


class TestMetaPeriod(object):
    def setup_class(self):
        self.start_time = datetime.datetime.now(datetime.timezone.utc)

    def test_process_trade(self):
        assert True

    def get_historical_data(self, num_periods=200):
        assert True
