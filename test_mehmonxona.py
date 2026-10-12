import unittest
from xona.xona_oop import Xona

test_xona = Xona(1,29999,4)
class XonaTest(unittest.TestCase):

    def test_xona(self):
        self.assertTrue(test_xona.band_mi())

    def test_mehmon(self):
        pass

