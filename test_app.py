# test_app.py
import unittest
from app import app, db, BlockedIP, RequestLog

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db

    def test_catch_all(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_unban(self):
        with app.app_context():
            ip = '192.0.2.0'
            blocked_ip = BlockedIP(ip_address=ip)
            db.session.add(blocked_ip)
            db.session.commit()

            self.app.cli_runner().invoke(args=['unban', ip])

            blocked_ip = BlockedIP.query.filter_by(ip_address=ip).first()
            self.assertIsNone(blocked_ip)

if __name__ == '__main__':
    unittest.main()