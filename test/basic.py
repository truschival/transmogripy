import unittest
import context
from transmogripy import TransmogriPy as TM

class TransmogrificationTests(unittest.TestCase):

    def test_basic_transmogrify(self):
        dut = TM.TransmogriPy(2)
        res = dut.transmogrify(3)
        self.assertEqual(res,11)

    def test_basic_banner(self):
        dut = TM.TransmogriPy(27)
        res = dut.banner();
        self.assertEqual(res,"Transmogrification constant = 27")


if __name__ == '__main__':
    unittest.main()
    
