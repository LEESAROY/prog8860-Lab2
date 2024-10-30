import unittest
from io import StringIO
import sys

class TestPrintOutput(unittest.TestCase):
    def test_print_output(self):
        # Redirect stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function
        print("This is Lab2")

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Check the output
        self.assertEqual(captured_output.getvalue().strip(), "This is Lab2")

if __name__ == '__main__':
    unittest.main()
