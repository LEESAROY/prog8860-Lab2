import unittest
from io import StringIO
import sys

class TestPrintOutput(unittest.TestCase):
    def test_print_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        print("This is Lab2")

        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "This is Lab2")

if __name__ == '__main__':
    unittest.main()
