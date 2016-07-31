import unittest


class PoopTest(unittest.TestCase):

    def setUp(self):
        self.fixture = range(1, 10)

    def tearDown(self):
        del self.fixture

    def test_fixture_is_range_1_to_10(self):
        self.assertEqual(self.fixture, range(1, 10))
