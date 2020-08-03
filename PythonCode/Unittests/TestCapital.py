import Capital
import unittest

class StringTest(unittest.TestCase):

    def test_capital_one_word(self):
        text = 'sara'
        result = Capital.capitalized(text)
        self.assertEquals(result,'Sara')

    def test_capital_multi_word(self):
        text = 'hey baby how are you?'
        result = Capital.capitalized(text)
        self.assertEquals(result,'Hey baby how are you?')

    def test_title_one_word(self):
        text ='moody'
        result = Capital.titled(text)
        self.assertEquals(result,'Moody')

    def test_title_multi_word(self):
        text = "Hey baby how are you and mother's car?"
        result = Capital.titled(text)
        self.assertEquals(result,"Hey Baby How Are You And Mother's Car?")



if __name__ == "__main__":
    unittest.main()