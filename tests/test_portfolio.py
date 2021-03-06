# -*- coding: utf-8 -*-
# vim:fenc=utf-8

'''
  :copyright (c) 2014 Xavier Bruhiere.
  :license: %LICENCE%, see LICENSE for more details.
'''

import unittest
from nose.tools import eq_, nottest
from portfolio.analytics import PortfolioAnalytics


class BasicPortfolio(PortfolioAnalytics):
    def optimize(signals, *args):
        return {}


class TestPortfolioObject(unittest.TestCase):

    @nottest
    def id_objective(self, x):
        return x

    def test_has_zipline_attributes(self):
        pf = BasicPortfolio()
        eq_(pf.positions, {})
        eq_(pf.start_date, None)
        for attribute in ['capital_used', 'cash', 'pnl',
                          'portfolio_value', 'positions_value',
                          'returns', 'starting_cash']:
            eq_(pf[attribute], 0.0)
