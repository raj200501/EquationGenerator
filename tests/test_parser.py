import unittest

from equation_generator.parser import parse_description, tokenize_description


class ParserTests(unittest.TestCase):
    def test_tokenize_description_basic(self):
        tokens = tokenize_description("five plus three equals eight")
        self.assertEqual(tokens, ["5", "+", "3", "=", "8"])

    def test_parse_description_power(self):
        result = parse_description("two to the power of three equals eight")
        self.assertEqual(result.equation, "2^{3} = 8")

    def test_parse_description_parentheses(self):
        result = parse_description(
            "open parenthesis five minus two close parenthesis times three"
        )
        self.assertEqual(result.equation, "( 5 - 2 ) \\cdot 3")


if __name__ == "__main__":
    unittest.main()
