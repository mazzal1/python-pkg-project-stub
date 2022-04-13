import unittest
from package.examples import example


class TestPackage(unittest.TestCase):

    def test_example(self):
        res = example.run()
        self.assertEqual(res, 1, "res equals 1")


if __name__ == '__main__':
    unittest.main()
