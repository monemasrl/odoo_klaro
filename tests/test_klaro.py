"""Tests for Klaro Module"""
from odoo.tests import common, tagged


class TestKlaroBase(common.SingleTransactionCase):
    """Base class used by TestKlaro"""

    @classmethod
    def setUpClass(cls):
        """setUp Class"""
        super().setUpClass()
        cls.partner = cls.env["res.partner"].create(
            {
                "name": "partner test contract",
                "email": "demo@demo.com",
            }
        )



class TestKlaro(TestKlaroBase):
    """Test suite for klaro module"""

    @tagged("klaro")
    def test_create_purposes(self):
        """Create purposes"""
        Purpose = self.env["klaro.purpose"]
        self.purpose1 = Purpose.create(
            {
                "name": "Test Purpose #1",
                "description": "Description of the Test Purpose #1",
                "title": "Title of the Test prupose #1",
            }
        )
        self.purpose2 = Purpose.create(
            {
                "name": "Test Purpose #1",
                "description": "Description of the Test Purpose #1",
                "title": "Title of the Test prupose #1",
            }
        )
        self.purposes = Purpose.search([])

        self.assertEqual(len(self.purposes), 2)
