import unittest 
from unittest import TestCase
from unittest.mock import patch, call

import bitcoin

class TestExchangeRate(TestCase):
    @patch('builtins.input', side_effect=['2'])
    def test_get_bitcoin_amount(self, mock_input):
        bitcoins = bitcoin.get_bitcoin_amount()
        self.assertEqual(bitcoins, '2')

    @patch('builtins.input', side_effect=['2'])
    def test_get_bitcoin_amount_not_equal(self, mock_input):
        bitcoins = bitcoin.get_bitcoin_amount()
        self.assertNotEqual(bitcoins, '5')

    @patch('bitcoin.get_bitcoin_data')
    def test_bitcoin_to_usd(self, mock_rates):
        mock_rate = 4.13
        example_api_response = {"bpi":{ "USD":{ "rate_float": mock_rate}}}
        mock_rates.side_effect = [ example_api_response ]

        bitcoins = 2
        usd = bitcoin.bitcoin_to_usd(bitcoins)

        self.assertEqual(8.26, usd)

    @patch('bitcoin.get_bitcoin_data')
    def test_bitcoin_to_usd_not_equal(self, mock_rates):
        mock_rate = 4.13
        example_api_response = {"bpi":{ "USD":{ "rate_float": mock_rate}}}
        mock_rates.side_effect = [ example_api_response ]

        bitcoins = 1
        usd = bitcoin.bitcoin_to_usd(bitcoins)

        self.assertNotEqual(8.26, usd)

    @patch('builtins.print')
    def test_display_results(self, mock_print):

        bitcoin.display_results('a', 'b', 'c')

        mock_print.assert_called_once_with('abc')