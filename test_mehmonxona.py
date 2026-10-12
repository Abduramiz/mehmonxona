import unittest
from mehmonxona.mehmonxona_oop import Xona , Mehmonxona


class XonaTest(unittest.TestCase):

    def setUp(self):
        self.test_xona = Xona(1, 10000, 4)

    def test_xona_bosh(self):
        self.assertTrue(self.test_xona.band_mi())

