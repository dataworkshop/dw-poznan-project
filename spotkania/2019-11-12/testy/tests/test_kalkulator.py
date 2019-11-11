from kalkulator.Kalkulator import Kalkulator


def test_dodaj():
    k = Kalkulator()
    assert k.dodaj(2,3) == 5

import unittest
import unittest.mock
from unittest.mock import patch, MagicMock


class test_kalulator_class(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(test_kalulator_class, self).__init__(*args,**kwargs)
        self.kaklulator = Kalkulator()

    def test_dodaj(self ):
        self.assertEqual( self.kaklulator.dodaj(2,3)  , 5)

    def test_dodaj_mock(self):
        k = Kalkulator()
        k.dodaj = MagicMock(return_value=5)
        self.assertEqual(k.dodaj(2,3), 5)
        self.assertEqual(k.dodaj(5,7), 5)

    @patch.object(Kalkulator, attribute='dodaj', return_value=5)
    def test_mock1(self, patch_object):
        k = Kalkulator()
        self.assertEqual(k.dodaj(5,4), 5)
