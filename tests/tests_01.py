import unittest

from techtest01.first_non_repeating_letter import first_non_repeating_letter


class TestFunctionToTest(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(first_non_repeating_letter("aabbcdd"), "c")
        self.assertEqual(first_non_repeating_letter("abcabc"), None)
        self.assertEqual(first_non_repeating_letter("swiss"), "w")
        self.assertEqual(first_non_repeating_letter(""), None)
        self.assertEqual(first_non_repeating_letter("abracadabra"), "c")


if __name__ == "__main__":
    unittest.main()
