# test_tradeinterface.py
"""
Tests for TradeInterface module.
"""

import unittest
from tradeinterface import TradeInterface

class TestTradeInterface(unittest.TestCase):
    """Test cases for TradeInterface class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TradeInterface()
        self.assertIsInstance(instance, TradeInterface)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TradeInterface()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
