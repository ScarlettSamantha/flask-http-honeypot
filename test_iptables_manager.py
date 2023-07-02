# test_iptables_manager.py
import unittest
from iptables_manager import IPTablesManager

class TestIPTablesManager(unittest.TestCase):
    def setUp(self):
        self.iptables_manager = IPTablesManager()

    def test_block_ip(self):
        # Test blocking an IP address
        result = self.iptables_manager.block_ip('192.0.2.0')
        self.assertTrue(result, "Failed to block IP address")

    def test_unblock_ip(self):
        # Test unblocking an IP address
        result = self.iptables_manager.unblock_ip('192.0.2.0')
        self.assertTrue(result, "Failed to unblock IP address")

    def test_block_invalid_ip(self):
        # Test blocking an invalid IP address
        result = self.iptables_manager.block_ip('999.999.999.999')
        self.assertFalse(result, "Managed to block an invalid IP address")

    def test_unblock_invalid_ip(self):
        # Test unblocking an invalid IP address
        result = self.iptables_manager.unblock_ip('999.999.999.999')
        self.assertFalse(result, "Managed to unblock an invalid IP address")

if __name__ == '__main__':
    unittest.main()